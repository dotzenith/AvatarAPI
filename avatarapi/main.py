"""
The main module for the api
"""

from fastapi import Query, Request

from avatarapi.app import make_app
from avatarapi.helpers import Quotes, make_custom_df
from avatarapi.schemas import *

# Some definitions for usage later
app = make_app()
Num = Query(10, ge=1, le=25, description="The number of quotes")


@app.get("/api/quotes", response_model=ReturnQuotes)
async def quotes(request: Request, num: int = Num):
    """
    Get 10 random quotes, or the specified number of quotes
    """

    quotes = Quotes.sample(n=num).to_dicts()
    return {"num": len(quotes), "quotes": quotes}


@app.get("/api/quotes/character", response_model=ReturnQuotes)
async def character(request: Request, name: Characters = Query(), num: int = Num):
    """
    Get quotes from a specific character
    """

    quotes = make_custom_df("Character", name, num)
    return {"num": len(quotes), "quotes": quotes}


@app.get("/api/quotes/nation", response_model=ReturnQuotes)
async def nation(request: Request, name: Nations = Query(), num: int = Num):
    """
    Get quotes from a specific nation
    """

    quotes = make_custom_df("Nation", name, num)
    return {"num": len(quotes), "quotes": quotes}


@app.get("/api/quotes/bending", response_model=ReturnQuotes)
async def bending(request: Request, bending: Bendings = Query(), num: int = Num):
    """
    Get quotes from a character with specific bending type
    """

    quotes = make_custom_df("Bending", bending, num)
    return {"num": len(quotes), "quotes": quotes}


@app.get("/api/quotes/episode", response_model=ReturnQuotes)
async def episode(request: Request, title: Episodes = Query(), num: int = Num):
    """
    Get quotes from a specific episode
    """

    quotes = make_custom_df("Episode", title, num)
    return {"num": len(quotes), "quotes": quotes}


@app.get("/api/quotes/book", response_model=ReturnQuotes)
async def book(request: Request, title: Books = Query(), num: int = Num):
    """
    Get quotes from a specific nation
    """

    quotes = make_custom_df("Book", title, num)
    return {"num": len(quotes), "quotes": quotes}
