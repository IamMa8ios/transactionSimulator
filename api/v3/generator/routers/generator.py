from typing import Annotated

from fastapi import APIRouter, status, Depends

from api.v3.generator.dependencies import get_generator_service
from api.v3.generator.services import GeneratorService

router = APIRouter(prefix="/api/v3/generator", tags=["Data Generator Management"])


@router.post("/customers", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
async def generate_customers(generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_customers()


@router.post("/customer_info", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
async def generate_customer_personal_info(
        generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_customer_personal_info()


@router.post("/products", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
async def generate_products(number_of_products: int,
                            generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_products(number_of_products)


@router.post("/product_variants", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
async def generate_product_variants(number_of_products: int, number_of_variants: int,
                                    generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_product_variants(number_of_products, number_of_variants)


@router.post("/customer_orders", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
def generate_customer_orders(number_of_orders: int,
                             generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_customer_orders(number_of_orders)


@router.post("/customer_order_items", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
def generate_customer_order_items(number_of_orders: int, number_of_items: int,
                                  generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_customer_order_items(number_of_orders, number_of_items)


@router.post("/aftersale_tickets", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
def generate_aftersale_tickets(number_of_tickets: int,
                               generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_aftersale_tickets(number_of_tickets)


@router.post("/customer_order_shipments", dependencies=[Depends(get_generator_service)],
             status_code=status.HTTP_201_CREATED)
def generate_customer_order_shipments(number_of_shipments: int,
                                      generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_customer_order_shipments(number_of_shipments)


@router.post("/backorder_shipments", dependencies=[Depends(get_generator_service)], status_code=status.HTTP_201_CREATED)
def generate_backorder_shipments(number_of_shipments: int,
                                 generator_service: Annotated[GeneratorService, Depends(get_generator_service)]):
    generator_service.generate_backorder_shipments(number_of_shipments)
