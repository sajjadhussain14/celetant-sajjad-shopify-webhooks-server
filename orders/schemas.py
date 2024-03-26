# schemas.py

from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: int
    created_at: Optional[str]  # Assuming it's a string representation of a timestamp
    currency: Optional[str]
    current_total_price: Optional[float]
    total_tax: Optional[float]
    total_discounts: Optional[float]
    customer_locale: Optional[str]
    financial_status: Optional[str]
    fulfillment_status: Optional[str]
    order_status_url: Optional[str]
    line_items: Optional[dict]
    tax_lines: Optional[dict]
    shipping_address: Optional[dict]
    customer: Optional[dict]
    
class OrderDisplay(BaseModel):
    id: int
    currency: Optional[str]
    current_total_price: Optional[float]
    total_tax: Optional[float]
    total_discounts: Optional[float]
    customer_locale: Optional[str]
    financial_status: Optional[str]
    fulfillment_status: Optional[str]
    order_status_url: Optional[str]
    line_items: Optional[dict]
    tax_lines: Optional[dict]
    shipping_address: Optional[dict]
    customer: Optional[dict]


