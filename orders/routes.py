# routes.py

from fastapi import APIRouter, HTTPException, Header
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()

class OrderPayload(BaseModel):
    id: str

@router.post("/webhooks/orders/create")
async def create_order_webhook(
    payload: OrderPayload):

    return {"message":"OK"}
    #return save_order(arguments_json)


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
