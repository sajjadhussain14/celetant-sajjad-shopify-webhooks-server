# routes.py

from fastapi import APIRouter, HTTPException, Header,Response,Request
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders,calculated_hmac
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()


@router.post("/webhooks/orders/create")
async def handle_webhook(request: Request):
    try:
        # Extract request data and HMAC header
        request_data = await request.body()
        hmac_header = request.headers.get('X-Shopify-Hmac-SHA256')

        # Decode bytes data to string
        request_data_str = request_data.decode('utf-8')
        
        # Parse JSON data
        order_data = json.loads(request_data_str)

        generated_hmac=calculated_hmac(order_data)
        # Verify HMAC integrity
        #if not verify_shopify_webhook(order_data, hmac_header):
            #raise HTTPException(status_code=501, detail="HMAC verification failed")


        # Save order to database
        save_order(generated_hmac,hmac_header)

        # Respond with success
        return {"message": "Order processed successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
