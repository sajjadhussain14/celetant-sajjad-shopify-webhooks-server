# routes.py

from fastapi import APIRouter, HTTPException, Header
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()


@router.post("/webhooks/orders/create")
async def handle_order_creation_webhook(
    payload: dict,
    HTTP_X_SHOPIFY_HMAC_SHA256: str = Header(None)
):
    try:
        # Validate payload
        if not payload:
            raise HTTPException(status_code=422, detail="Payload is required")
        
        required_fields = ["id", "line_items"]  # Define required fields in the payload
        missing_fields = [field for field in required_fields if field not in payload]
        if missing_fields:
            raise HTTPException(status_code=422, detail=f"Missing fields in payload: {', '.join(missing_fields)}")
        
        # Validate header
        if not HTTP_X_SHOPIFY_HMAC_SHA256:
            raise HTTPException(status_code=422, detail="Missing 'X-Shopify-Hmac-Sha256' header")
        
        # Process the order payload
        # For example, you can access payload['id'], payload['line_items'], etc.
        
        return {"message": "Webhook received and processed successfully"}
    
    except HTTPException as e:
        # If an HTTPException was raised, return the exception response
        raise e
    
    except Exception as e:
        # Handle any unexpected errors
        # You can log the error, return a custom error response, etc.
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
