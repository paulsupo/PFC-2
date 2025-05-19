from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from src.routes import (
    executor_agent,
)


load_dotenv()

app = FastAPI()

app.include_router(executor_agent.router)