# services.py

from .schemas import Order,OrderDisplay
from db.connection import conn
import hmac
import hashlib
import psycopg2
import json
import base64
from datetime import datetime


CLIENT_SECRET = "c72c3df7dcb6c38b68a9e8cf225aec964e5febed202dc025873691cf085d5eb9"

def calculated_hmac(order):
    # Calculate HMAC
    calculated_hmac = hmac.new(CLIENT_SECRET.encode('utf-8'), order.encode('utf-8'), hashlib.sha256).digest()
    # Base 64 encoding
    calculated_hmac_base64 = base64.b64encode(calculated_hmac).decode('utf-8')
    return calculated_hmac_base64

def verify_shopify_webhook(data, hmac_header) :
    digest = hmac.new(CLIENT_SECRET.encode('utf-8'), data, digestmod=hashlib.sha256).digest()
    computed_hmac = base64.b64encode(digest)

    return hmac.compare_digest(computed_hmac, hmac_header.encode('utf-8'))

def save_order(data):
    # Save order to database
    request_data = data.decode('utf-8')

    # Parse JSON data
    order_json_data = json.loads(request_data)

    try:
        query = """
        INSERT INTO orders (id, created_at, currency, current_total_price, total_tax, total_discounts, customer_locale, financial_status, fulfillment_status, order_status_url, line_items, tax_lines, shipping_address, customer)
        VALUES (%(id)s, %(created_at)s, %(currency)s, %(current_total_price)s, %(total_tax)s, %(total_discounts)s, %(customer_locale)s, %(financial_status)s, %(fulfillment_status)s, %(order_status_url)s, %(line_items)s, %(tax_lines)s, %(shipping_address)s, %(customer)s)
        RETURNING id
        """

        # Adjust the values
        values = {
            'id': order_json_data['id'],
            'created_at': order_json_data['created_at'],
            'currency': order_json_data['currency'],
            'current_total_price': order_json_data['current_total_price'],
            'total_tax': order_json_data['total_tax'],
            'total_discounts': order_json_data['total_discounts'],
            'customer_locale': order_json_data['customer_locale'],
            'financial_status': order_json_data['financial_status'],
            'fulfillment_status': order_json_data['fulfillment_status'],
            'order_status_url': order_json_data['order_status_url'],
            'line_items': json.dumps(order_json_data['line_items']),
            'tax_lines': json.dumps(order_json_data['tax_lines']),
            'shipping_address': json.dumps(order_json_data['shipping_address']),
            'customer': json.dumps(order_json_data['customer'])
        }

        # Execute the query
        with conn.cursor() as cur:
            cur.execute(query, values)
            saved_order_id = cur.fetchone()  # Fetching the ID of the inserted order
            conn.commit()

            return {"status_code": 200, "data": "", "message": "Order saved successfully"}
    except psycopg2.Error as e:
        return {"status_code": 400, "data": None, "message": str(e)}
    
    

def get_orders():
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM orders
    """
    orders_data = {}
    try:
        cursor.execute(query,)
        orders_data = cursor.fetchall()        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

    orders = []
    for row in orders_data:
        order = OrderDisplay(
            id=row[0],
            currency=row[2],
            current_total_price=row[3],
            total_tax=row[4],
            total_discounts=row[5],
            customer_locale=row[6],
            financial_status=row[7],
            fulfillment_status=row[8],
            order_status_url=row[9],
            line_items=row[10],
            tax_lines=row[11],
            shipping_address=row[12],
            customer=row[13]
        )
        orders.append(order)

    return orders
