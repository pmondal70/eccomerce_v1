# from fastapi import APIRouter, Depends
# from pydantic import BaseModel
# from events.publisher import publish_order_created
# from utils.auth import get_current_user

# router = APIRouter()

# class OrderRequest(BaseModel):
#     item_id: int
#     quantity: int

# @router.post("/orders")
# def create_order(order: OrderRequest, user: dict = Depends(get_current_user)):
#     order_id = 123
#     publish_order_created(order_id, order.item_id, order.quantity)
#     return {"message": "Order created", "order_id": order_id}



from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.order import Order, get_db
from events.publisher import publish_order_created # absolute import path

# from ..models.order import Order, get_db # relative import path
from utils.auth import get_current_user


router = APIRouter()

class OrderRequest(BaseModel):
    item_id: int
    quantity: int

@router.post("/orders")
def create_order(order: OrderRequest, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    new_order = Order(item_id=order.item_id, quantity=order.quantity, user_id=user["id"])  # Replace with actual user ID from auth
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # publish_order_created(new_order.id, new_order.item_id, new_order.quantity)
    return {"message": "Order created", "order_id": new_order.id}

