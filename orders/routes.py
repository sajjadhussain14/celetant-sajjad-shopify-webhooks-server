# routes.py

from fastapi import APIRouter, HTTPException, Header,Response
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()

SENTINEL = "__X_SHOPIFY_HMAC_SHA256_NOT_PROVIDED__"

@router.post("/webhooks/orders/create")
async def handle_order_creation_webhook(
    payload: dict,
    X_Shopify_Hmac_SHA256: str = Header(SENTINEL, convert_underscores=False)
):
    
    if X_Shopify_Hmac_SHA256 == SENTINEL:
        raise HTTPException(status_code=404, detail="Missing 'X-Shopify-Hmac-SHA256' header")

    if not verify_shopify_webhook(payload, X_Shopify_Hmac_SHA256):
        payload={"message":"Invalid Shopify webhook"}
        raise HTTPException(status_code=401, detail="Invalid Shopify webhook")

    return save_order(payload)
    


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
