from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from json import load

app = FastAPI()

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


@app.get("/fooditems")
async def get():
    with open('./foodItems.json') as fp:
        items = load(fp)
        return items
