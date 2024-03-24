# main.py

from fastapi import FastAPI
from orders.routes import router as orders_router
import hmac
import hashlib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "https://bidsforce-client-phi.vercel.app",
    "http://localhost:3000",
        "http://127.0.0.1:3000",

    
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def server():
    # Your shared secret key
    shared_secret_key = "sajjad123"

    # Payload of the request
    order = {
    "order_id":"133",
    "customer_id":"3",
    "total_price":333
}

    return hmac.new(shared_secret_key.encode('utf-8'), str(order).encode('utf-8'), hashlib.sha256).hexdigest()


app.include_router(orders_router, prefix="/api/v1")
