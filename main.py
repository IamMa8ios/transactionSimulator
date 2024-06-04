from fastapi import FastAPI

from api.v2.customer import router as customer_router
from api.v2.product import router as product_router
from api.v1.order.router import router as order_router
from api.v1.emulator.router import router as emulator_router

app = FastAPI()

app.include_router(customer_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(emulator_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
