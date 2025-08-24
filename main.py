"""Main module for the FastAPI application.

This module defines the API endpoints and related logic.
"""

# Import Annotated for type hinting with metadata in FastAPI endpoints
from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(description="This is a simple API to test the FastAPI framework")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends[oauth2_scheme]]):
    """Get items from the API"""
    return {"token": token}
