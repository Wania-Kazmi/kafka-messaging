from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from kafka.router_file import consume, route
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print("Initializing...")
    asyncio.create_task(consume())
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Hello World API with Kafka",
    version="0.0.1",
    servers=[
        {
            "url": "http://localhost:8000/",  # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ]
)

app.include_router(route)

@app.get('/')
async def Home():
    return "welcome home"

