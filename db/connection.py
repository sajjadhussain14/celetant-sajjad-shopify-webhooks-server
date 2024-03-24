# db/connection.py

import psycopg2

conn = psycopg2.connect(
dbname="verceldb",
user="default",
password="3yHMjDYeZ0VO",
host="ep-bitter-heart-a4t4x9yx-pooler.us-east-1.aws.neon.tech",
port="5432"
)

