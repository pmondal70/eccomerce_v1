from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.product import Product, get_db, Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()

class ProductRequest(BaseModel):
    name: str
    description: str = ""
    price: float
    stock: int = 0

@router.post("/products")
def create_product(product: ProductRequest, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/products")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product