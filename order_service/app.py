from fastapi import FastAPI
from routes.orders import router as orders_router
from utils.auth import jwt_manager

app = FastAPI(title="Ecommerce Service")
app.include_router(orders_router, prefix="/orders", tags=["orders"])
jwt_manager(app)
