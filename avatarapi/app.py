"""
Dedicated module to construct fastapi app
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address


def make_app() -> FastAPI:
    """
    Makes fastapi app with rate limiter and CORS
    """

    app = FastAPI(docs_url=None, redoc_url=None)

    limiter = Limiter(key_func=get_remote_address, default_limits=["100/hour"])
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["GET"],
    )

    return app
