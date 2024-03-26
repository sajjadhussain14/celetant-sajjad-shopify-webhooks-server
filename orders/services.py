# services.py

from .schemas import Order
from db.connection import conn
import hmac
import hashlib
import psycopg2
import json
import base64


shared_secret_key = "c72c3df7dcb6c38b68a9e8cf225aec964e5febed202dc025873691cf085d5eb9"

def calculated_hmac(order):
    # Calculate HMAC
    calculated_hmac = hmac.new(shared_secret_key.encode('utf-8'), order.encode('utf-8'), hashlib.sha256).digest()
    # Base 64 encoding
    calculated_hmac_base64 = base64.b64encode(calculated_hmac).decode('utf-8')
    return calculated_hmac_base64

def verify_shopify_webhook(order, hmac_header) :
    calculated_hmac = hmac.new(shared_secret_key.encode('utf-8'), str(order).encode('utf-8'), hashlib.sha256).hexdigest()
    return hmac.compare_digest(calculated_hmac, hmac_header)

def save_order(data_string,hmac_header,generated_hmac):

    try:
        query = """
        INSERT INTO orders (data, header_hmac, generated_hmac)
        VALUES (%s, %s, %s)
        RETURNING data, header_hmac, generated_hmac
        """
        values = (data_string, hmac_header, generated_hmac)
        with conn.cursor() as cur:
            cur.execute(query, values)
            saved_order = cur.fetchone()
            conn.commit()
            conn.close()

            return {"status_code": 200, "data": "", "message": "Order saved successfully"}
    except psycopg2.Error as e:
        return {"status_code": 400, "data": None, "message": str(e)}
    
    

def get_orders():
    cursor = conn.cursor()

    query = "SELECT order_id, customer_id, total_price FROM orders"
    orders_data = {}
    try:
        cursor.execute(query, )
        orders_data = cursor.fetchall()        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


    return [
        Order(
            order_id=row[0],
            customer_id=row[1],
            total_price=row[2]
        )
        for row in orders_data
    ]

