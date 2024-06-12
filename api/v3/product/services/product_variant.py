from api.v3.product.repositories import ProductVariantRepository
from api.v3.product.schemas import ProductVariantUpdate, ProductVariantCreate, ProductVariantRead
from api.v3.templates import CRUDService


class ProductVariantService(CRUDService[ProductVariantCreate, ProductVariantRead, ProductVariantUpdate,
                            ProductVariantRepository]):

    def __init__(self, product_variant_repository: ProductVariantRepository):
        super().__init__(product_variant_repository)
