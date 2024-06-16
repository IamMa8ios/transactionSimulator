from fastapi import FastAPI

from api.v3.customer.routers import customer_router, customer_personal_info_router
from api.v3.product.routers import product_router, product_variant_router
from api.v3.customer_order.routers import customer_order_router, customer_order_item_router, aftesale_ticket_router
from api.v3.shipment.routers import customer_order_shipment_router, backorder_shipment_router
from api.v3.generator.routers import generator_router

app = FastAPI()

app.include_router(customer_router)
app.include_router(customer_personal_info_router)
app.include_router(product_router)
app.include_router(product_variant_router)
app.include_router(customer_order_router)
app.include_router(customer_order_item_router)
app.include_router(aftesale_ticket_router)
app.include_router(customer_order_shipment_router)
app.include_router(backorder_shipment_router)
app.include_router(generator_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
