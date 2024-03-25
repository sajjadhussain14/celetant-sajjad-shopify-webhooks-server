# routes.py

from fastapi import APIRouter, HTTPException, Header,Response
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()


@router.post("/webhooks/orders/create")
async def handle_order_creation_webhook(
    payload: dict,
    X_Shopify_Hmac_SHA256: str = Header(None, convert_underscores=False)
):
        
    return Response(status_code=200)
    


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
