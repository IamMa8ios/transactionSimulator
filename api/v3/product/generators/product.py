import random

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from api.v3.db import engine
from api.v3.product.repositories import ProductRepository
from api.v3.product.schemas import ProductCreate
from api.v3.product.models import Product, ProductVariant
from api.v3.shipment.models import CustomerOrderShipment, BackorderShipment
from api.v3.customer_order.models import CustomerOrder, CustomerOrderItem


types = ["Electronics", "Clothing", "Home", "Beauty", "Toys", "Sports", "Books", "Groceries", "Automotive", "Garden"]
brands = [
    "ElectroBuzz", "Techies", "GadgetPro", "WiredWorld", "CircuitSaviors",
    "FashionFinesse", "Trendsetters", "StyleHub", "VogueVentures", "ChicChamps",
    "HomeHarmony", "ComfyNest", "CasaBliss", "DecorDazzle", "LivingLuxe",
    "BeautifyMe", "GlowGurus", "RadiantYou", "CharmChamps", "GlamGurus",
    "ToyTreasures", "PlayParadise", "FunFoundry", "GameGenius", "ToyTrove",
    "SportySpree", "FitFables", "ActiveAces", "PlayPros", "SportSphere",
    "BookBounty", "ReadRangers", "PagePioneers", "NovelNook", "LiteraryLegends",
    "GroceryGurus", "FreshFinds", "PantryPros", "SnackSages", "MarketMavens",
    "AutoAces", "CarCareCrew", "MotorMasters", "DriveDazzle", "RideRangers",
    "GardenGurus", "GreenThumbs", "PlantPros", "BloomBuddies", "NatureNurturers"
]
categories = ["Electronics", "Fashion", "Home & Kitchen", "Health & Beauty", "Toys & Games", "Sports & Outdoors",
              "Books", "Groceries", "Automotive", "Garden & Outdoors"]
subcategories = {
    "Electronics": ["Smartphones", "Laptops", "Headphones", "Cameras", "Wearables"],
    "Fashion": ["Men", "Women", "Kids", "Accessories", "Footwear"],
    "Home & Kitchen": ["Furniture", "Appliances", "Decor", "Kitchenware", "Bedding"],
    "Health & Beauty": ["Makeup", "Skincare", "Haircare", "Fragrance", "Wellness"],
    "Toys & Games": ["Action Figures", "Board Games", "Dolls", "Educational", "Puzzles"],
    "Sports & Outdoors": ["Fitness Equipment", "Outdoor Gear", "Sportswear", "Footwear", "Accessories"],
    "Books": ["Fiction", "Non-Fiction", "Children's Books", "Educational", "Comics"],
    "Groceries": ["Fresh Produce", "Snacks", "Beverages", "Dairy", "Pantry Staples"],
    "Automotive": ["Car Accessories", "Maintenance Tools", "Car Care", "Electronics", "Safety"],
    "Garden & Outdoors": ["Plants", "Gardening Tools", "Outdoor Furniture", "Grills", "Decor"]
}
brand_mapping = {
    "Electronics": ["ElectroBuzz", "Techies", "GadgetPro", "WiredWorld", "CircuitSaviors"],
    "Clothing": ["FashionFinesse", "Trendsetters", "StyleHub", "VogueVentures", "ChicChamps"],
    "Home": ["HomeHarmony", "ComfyNest", "CasaBliss", "DecorDazzle", "LivingLuxe"],
    "Beauty": ["BeautifyMe", "GlowGurus", "RadiantYou", "CharmChamps", "GlamGurus"],
    "Toys": ["ToyTreasures", "PlayParadise", "FunFoundry", "GameGenius", "ToyTrove"],
    "Sports": ["SportySpree", "FitFables", "ActiveAces", "PlayPros", "SportSphere"],
    "Books": ["BookBounty", "ReadRangers", "PagePioneers", "NovelNook", "LiteraryLegends"],
    "Groceries": ["GroceryGurus", "FreshFinds", "PantryPros", "SnackSages", "MarketMavens"],
    "Automotive": ["AutoAces", "CarCareCrew", "MotorMasters", "DriveDazzle", "RideRangers"],
    "Garden": ["GardenGurus", "GreenThumbs", "PlantPros", "BloomBuddies", "NatureNurturers"]
}


def generate_product_data(num_products):

    with Session(engine) as session:
        product_repository = ProductRepository(session)
        total = 0
        while total < num_products:
            product_type = random.choice(types)
            brand = random.choice(brand_mapping.get(product_type, brands))
            category = random.choice(categories)
            subcategory = random.choice(subcategories.get(category, ["General"]))
            title = f"{product_type} in {subcategory} product by {brand}"
            description = (f"This {product_type} product by {brand} is perfect for anyone looking to enhance their "
                           f"experience with top-quality {product_type.lower()} items.")
            price = round(random.uniform(5.0, 1000.0), 2)
            cost = round(price * random.uniform(0.5, 0.8), 2)

            product = ProductCreate(
                type=product_type,
                title=title,
                brand=brand,
                description=description,
                category=category,
                subcategory=subcategory,
                price=price,
                cost=cost
            )

            try:
                product_repository.create(product)
                total += 1
            except IntegrityError:
                # print(f"IntegrityError: {e}")
                session.rollback()


# generate_product_data(100)
