# routes.py

from fastapi import APIRouter, HTTPException, Header
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header

router = APIRouter()

@router.post("/webhooks/orders/create")
async def create_order_webhook(
    order: dict,
    x_shopify_hmac_sha256: str = Header(None, convert_underscores=False)
):
    if x_shopify_hmac_sha256 is None:
        raise HTTPException(status_code=400, detail="Missing x_shopify_hmac_sha256 header")

    if not verify_shopify_webhook(order, x_shopify_hmac_sha256):
        raise HTTPException(status_code=401, detail="Invalid Shopify webhook")

    return save_order(order)


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
