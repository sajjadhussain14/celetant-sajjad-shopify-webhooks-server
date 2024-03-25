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
    try:
        data = await request.body()
        hmac_header = request.headers.get('X-Shopify-Hmac-SHA256')

        # Decode bytes data to string
        data_str = data.decode('utf-8')

        # Parse JSON data
        order_data = json.loads(data_str)
        order_json = json.dumps(order_data)
        formatted_data_string = "'" + order_json + "'"

        # Save order to database
        # save_order(order_data, hmac_header)

        Response("",status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
