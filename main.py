from fastapi import FastAPI, Depends, HTTPException,Response,status
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import Products
from sqlalchemy import create_engine 
from database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/product")
def get(db: Session = Depends(get_db)):
    all_products = db.query(models.Product).all()
    return all_products
 

@app.post("/product")
def create(product: Products, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.delete("/product/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    delete_post = db.query(models.Product).filter(models.Product.id == id).first()
    if delete_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    else:
        db.delete(delete_post)  
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/product/{id}")
def update(id:int ,product:Products, db:Session = Depends(get_db)):
    updated_post = db.query(models.Product).filter(models.Product.id==id)
    updated_post.first()
    
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f'post with such id:{id} does not exist')
    else:
        updated_post.update(product.dict(), synchronize_session=False)
        db.commit()
        return updated_post.first()