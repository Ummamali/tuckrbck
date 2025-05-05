from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from FlatFileCollection import FlatFileCollection
from CRUDRoutes import CRUDRoutes
from order_schema import Order, OrderUpdate

app = FastAPI()

# database
orders_database = FlatFileCollection('orders.json')
food_items_database = FlatFileCollection('foodItems.json')
users_database = FlatFileCollection('users.json')

# List of allowed origins
origins = [
    "http://localhost:5173",
]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],     # GET, POST, etc.
    allow_headers=["*"],     # Accept, Content-Type, etc.
)

# static files
app.mount("/static", StaticFiles(directory='public'), name='static')


# Creating basic CRUD routes
food_item_router = CRUDRoutes(database=food_items_database, route_code='R')
order_router = CRUDRoutes(
    database=orders_database, ObjectSchema=Order, ObjectUpdateSchema=OrderUpdate)
users_router = CRUDRoutes(database=users_database, route_code='R')


# Mounting them
app.include_router(food_item_router.get_router(), prefix='/fooditems')
app.include_router(order_router.get_router(), prefix='/orders')
app.include_router(users_router.get_router(), prefix='/users')
