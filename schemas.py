from pydantic import BaseModel

class Products(BaseModel):
    id: int
    title: str
    description: str
    at_sales: bool
    inventory: int
