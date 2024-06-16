from api.v3.generator.repositories import GeneratorRepository


class GeneratorService:

    def __init__(self, generator_repository: GeneratorRepository):
        self.generator_repository = generator_repository

    def generate_customers(self):
        self.generator_repository.generate_customers()

    def generate_customer_personal_info(self):
        self.generator_repository.generate_customer_personal_info()

    def generate_products(self, number_of_products: int = 10):
        self.generator_repository.generate_products(number_of_products)

    def generate_product_variants(self, number_of_products: int = 1, number_of_variants: int = 3):
        self.generator_repository.generate_product_variants(number_of_products, number_of_variants)

    def generate_customer_orders(self, number_of_orders: int = 3):
        self.generator_repository.generate_customer_orders(number_of_orders)

    def generate_customer_order_items(self, number_of_orders: int = 1, number_of_items: int = 3):
        self.generator_repository.generate_customer_order_items(number_of_orders, number_of_items)

    def generate_aftersale_tickets(self, number_of_tickets: int = 1):
        self.generator_repository.generate_aftersale_tickets(number_of_tickets)

    def generate_customer_order_shipments(self, number_of_shipments: int = 1):
        self.generator_repository.generate_customer_order_shipments(number_of_shipments)

    def generate_backorder_shipments(self, number_of_shipments: int = 1):
        self.generator_repository.generate_backorder_shipments(number_of_shipments)
