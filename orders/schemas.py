# schemas.py

from pydantic import BaseModel

class Order(BaseModel):
    order_id: str
    customer_id: str
    total_price: float

    class Config:
        orm_mode = True
