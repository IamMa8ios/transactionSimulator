from api.v3.product.models import Product
from api.v3.product.repositories import ProductRepository
from api.v3.product.schemas import ProductCreate, ProductRead, ProductUpdate
from api.v3.templates import CRUDService


class ProductService(CRUDService[Product, ProductCreate, ProductRead, ProductUpdate, ProductRepository]):

    def __init__(self, product_repository: ProductRepository):
        super().__init__(product_repository)
