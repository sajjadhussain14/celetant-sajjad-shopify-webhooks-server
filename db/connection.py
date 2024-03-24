# db/connection.py

import psycopg2

conn = psycopg2.connect(
dbname="shopify",
user="postgres",
password="123456",
host="localhost",
port="5432"
)

