from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    category_id: int
