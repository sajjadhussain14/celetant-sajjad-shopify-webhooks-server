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
from fastapi.encoders import jsonable_encoder
CLIENT_SECRET = "c72c3df7dcb6c38b68a9e8cf225aec964e5febed202dc025873691cf085d5eb9"

router = APIRouter()


def verify_webhook(data, hmac_header):
    digest = hmac.new(CLIENT_SECRET.encode('utf-8'), data, digestmod=hashlib.sha256).digest()
    computed_hmac = base64.b64encode(digest)

    return hmac.compare_digest(computed_hmac, hmac_header.encode('utf-8'))


@router.post("/webhooks/orders/create")
async def handle_webhook(request: Request):
    try:
        data = await request.body()
        verified = verify_webhook(data, request.headers.get('X-Shopify-Hmac-SHA256'))

        # Save order to database
        save_order(str(verified),str(verified),str(verified))

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
