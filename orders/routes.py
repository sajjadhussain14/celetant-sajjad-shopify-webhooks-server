# routes.py

from fastapi import APIRouter, HTTPException, Header
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json

router = APIRouter()

@router.post("/webhooks/orders/create")
async def create_order_webhook(
    **kwargs):
    arguments_json = json.dumps(kwargs)


    return save_order(arguments_json)


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
