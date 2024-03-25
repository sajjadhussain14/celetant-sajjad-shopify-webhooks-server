# routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .services import verify_shopify_webhook, save_order, get_orders

router = APIRouter()

class LineItem(BaseModel):
    id: str
    title: str
    price: float
    quantity: int

class OrderPayload(BaseModel):
    id: str
    line_items: list[LineItem]  # Assuming line items is a list of LineItem objects

@router.post("/webhooks/orders/create")
async def create_order_webhook(payload: OrderPayload):
    # Process the order payload here
    # For example, you can access payload.id, payload.line_items, etc.
    # Then you can save the order or perform any other necessary actions
    
    return {"message": "Order webhook received and processed successfully"}

@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
