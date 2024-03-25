# routes.py

from fastapi import APIRouter, HTTPException, Header
from .schemas import Order
from .services import verify_shopify_webhook, save_order, get_orders
from fastapi import Header
import json
from pydantic import BaseModel

router = APIRouter()

from typing import List, Optional

class Address(BaseModel):
    first_name: str
    address1: str
    phone: str
    city: str
    zip: str
    province: str
    country: str
    last_name: str
    company: str
    name: str
    country_code: str
    province_code: str

class LineItem(BaseModel):
    id: str
    admin_graphql_api_id: str
    current_quantity: int
    fulfillment_service: str
    grams: int
    name: str
    price: str
    product_id: int
    quantity: int
    requires_shipping: bool
    sku: str
    taxable: bool
    title: str
    variant_id: int
    variant_inventory_management: str

class ShippingLine(BaseModel):
    id: int
    discounted_price: str
    price: str
    title: str

class Customer(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    state: str
    default_address: Address

class OrderPayload(BaseModel):
    id: int
    buyer_accepts_marketing: bool
    cancel_reason: str
    cancelled_at: str
    contact_email: str
    created_at: str
    currency: str
    current_subtotal_price: str
    current_total_discounts: str
    current_total_price: str
    current_total_tax: str
    customer_locale: str
    email: str
    financial_status: str
    fulfillment_status: str
    landing_site: Optional[str]
    location_id: Optional[int]
    name: str
    note: Optional[str]
    order_number: int
    order_status_url: str
    presentment_currency: str
    processed_at: Optional[str]
    subtotal_price: str
    tags: str
    test: bool
    token: str
    total_discounts: str
    total_line_items_price: str
    total_outstanding: str
    total_price: str
    total_tax: str
    total_tip_received: str
    total_weight: int
    updated_at: str
    billing_address: Address
    customer: Customer
    line_items: List[LineItem]
    shipping_address: Address
    shipping_lines: List[ShippingLine]

@router.post("/webhooks/orders/create")
async def create_order_webhook(payload: OrderPayload):
    # Process the order payload here
    # For example, you can access payload.id, payload.line_items, etc.
    return {"message": "Order webhook received and processed successfully"}


@router.get("/orders")
async def get_orders_route():
    return get_orders()

@router.get("/test")
async def test():
    return {"message":"Hello Test"}
