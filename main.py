from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import *
app = FastAPI()

# Временные хранилища данных
products = []
categories = []

# Маршруты для категорий

@app.get("/categories/", response_model=List[Category])
def get_categories():
    return categories

@app.post("/categories/", response_model=Category)
def add_category(category: Category):
    categories.append(category)
    return category

@app.get("/categories/{category_id}", response_model=Category)
def get_category(category_id: int):
    for category in categories:
        if category.id == category_id:
            return category
    raise HTTPException(status_code=404, detail="Category not found")

# Маршруты для продуктов

@app.get("/products/", response_model=List[Product])
def get_products(
    category_id: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
):
    result = products
    if category_id is not None:
        result = [product for product in result if product.category_id == category_id]
    if min_price is not None:
        result = [product for product in result if product.price >= min_price]
    if max_price is not None:
        result = [product for product in result if product.price <= max_price]
    return result

@app.post("/products/", response_model=Product)
def add_product(product: Product):
    products.append(product)
    return product

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for i, product in enumerate(products):
        if product.id == product_id:
            products[i] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int):
    for i, product in enumerate(products):
        if product.id == product_id:
            return products.pop(i)
    raise HTTPException(status_code=404, detail="Product not found")

