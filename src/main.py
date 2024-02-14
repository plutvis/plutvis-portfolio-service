from contextvars import ContextVar
from typing import Final, Optional
from uuid import uuid4

from fastapi import FastAPI, Request
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import scoped_session, sessionmaker

from src.users.router import router

REQUEST_ID_CTX_KEY: Final[str] = "request_id"
_request_id_ctx_var: ContextVar[Optional[str]] = ContextVar(REQUEST_ID_CTX_KEY, default=None)

app = FastAPI()

app.include_router(router)

engine = create_async_engine('postgresql+asyncpg://plutvistest:plutvistest@localhost/plutvistest')


def get_request_id() -> Optional[str]:
    return _request_id_ctx_var.get()


@app.middleware('http')
async def db_session_middleware(req: Request, call_next):
    request_id = str(uuid4())
    ctx_token = _request_id_ctx_var.set(request_id)
    session = scoped_session(sessionmaker(bind=engine, class_=AsyncSession), scopefunc=get_request_id)
    try:
        req.state.session = session
        response = await call_next(req)
    finally:
        await session.close()

    _request_id_ctx_var.reset(ctx_token)
    return response
