# routes.py

from fastapi import APIRouter, HTTPException, Header
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()


@router.post("/webhooks/orders/create")
async def handle_order_creation_webhook(payload: dict, X_Shopify_Hmac_Sha256: str = Header(None)):
    # Process the order payload here
    # For example, you can access payload.id, payload.line_items, etc.
    return {"message": payload}


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
