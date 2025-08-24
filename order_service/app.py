from fastapi import FastAPI
from routes.orders import router as orders_router
from routes.products import router as products_router
from utils.auth import jwt_manager

app = FastAPI(title="Ecommerce Service")
app.include_router(orders_router, prefix="/orders", tags=["orders"])
app.include_router(products_router, prefix="/products", tags=["products"])
jwt_manager(app)
