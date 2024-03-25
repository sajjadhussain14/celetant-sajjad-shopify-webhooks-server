# routes.py

from fastapi import APIRouter, HTTPException, Header,Response,Request
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()


@router.post("/webhooks/orders/create")
async def handle_webhook(request: Request):
    data = await request.body()
    hmac_header = request.headers.get('X-Shopify-Hmac-SHA256')
    
    Response("",status_code=200)

@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
