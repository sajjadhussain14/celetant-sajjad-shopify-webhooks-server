# routes.py

from fastapi import APIRouter, HTTPException, Header,Response,Request
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders,calculated_hmac
from fastapi import Header
import json
from pydantic import BaseModel
import hmac
import hashlib
import base64

router = APIRouter()


@router.post("/webhooks/orders/create")
async def handle_webhook(request: Request):
    try:
        # Extract request data and HMAC header
        request_data = await request.body()
        hmac_header = request.headers.get('X-Shopify-Hmac-SHA256')
        #gKot9BLD7WV4sKQeDGEzUlxQw+J7rgJfoZDiEEE+XHs=

        # Decode bytes data to string
        request_data_str = request_data.decode('utf-8')
        
        # Parse JSON data
        order_data = json.loads(request_data_str)
        data_json_string = json.dumps(order_data)
        data_string = f"'{data_json_string}'"
        

        # Calculate HMAC
        calculated_hmac_base64 = calculated_hmac(data_string)

        is_matched=""
        if hmac_header is None :
            is_matched = "khali"
        elif hmac.compare_digest(calculated_hmac_base64, hmac_header)==True:
            is_matched = str(True)
        else:
            is_matched = str(False)

        
        # Verify HMAC integrity
        #if not verify_shopify_webhook(order_data, hmac_header):
            #raise HTTPException(status_code=501, detail="HMAC verification failed")

        # Save order to database
        save_order(data_string,is_matched,is_matched)

        # Respond with success
        return {"message": 200}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
