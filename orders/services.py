# services.py

from fastapi import APIRouter, HTTPException, Header,Response
from .schemas import Order
from db.connection import conn
import hmac
import hashlib
import psycopg2
import json


shared_secret_key = "c72c3df7dcb6c38b68a9e8cf225aec964e5febed202dc025873691cf085d5eb9"

def verify_shopify_webhook(order: dict, hmac_header: str) :
    calculated_hmac = hmac.new(shared_secret_key.encode('utf-8'), str(order).encode('utf-8'), hashlib.sha256).hexdigest()
    return hmac.compare_digest(calculated_hmac, hmac_header)

def save_order(order_data, hmac_header):
    #order_json = json.dumps(order_data)
    #formatted_data_string = "'" + order_json + "'"

    query = """
    INSERT INTO orders (order_id, customer_id, total_price)
    VALUES (%s, %s, %s)
    RETURNING order_id, customer_id, total_price
    """
    values = ('formatted_data_string', "88", 99)
    with conn.cursor() as cur:
        cur.execute(query, values)
        saved_order = cur.fetchone()
        conn.commit()
        conn.close()

    return {"oder_id":""}
    
    

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

