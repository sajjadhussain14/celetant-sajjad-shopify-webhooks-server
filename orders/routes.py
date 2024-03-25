# routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError
from .services import verify_shopify_webhook, save_order, get_orders

router = APIRouter()

class LineItem(BaseModel):
    id: str
    title: str
    price: float
    quantity: int

class OrderPayload(BaseModel):
    id: str
    line_items: list[LineItem]  # Assuming line items is a list of LineItem objects

@router.post("/webhooks/orders/create")
async def create_order_webhook(payload: OrderPayload):
    try:
        # Process the order payload here
        # For example, you can access payload.id, payload.line_items, etc.
        # Then you can save the order or perform any other necessary actions
        # return save_order(arguments_json)

        return {"message": "Order webhook received and processed successfully"}
    except ValidationError as e:
        # Validation error occurred, return informative error message
        detail = e.errors()[0]['msg']
        raise HTTPException(status_code=422, detail=detail)
    except Exception as e:
        # Other unexpected error occurred, return generic error message
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
