from redis.asyncio import Redis
from litestar import Litestar, get
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import StoplightRenderPlugin

r = Redis(host='redis', port=6379, db=0)


@get("/")
async def index() -> dict[str, str]:
    return {"response": "ok"}


@get("/redis")
async def get_redis() -> dict[str, str]:
    # get hello from redis, if not exists, set hello to redis
    hello = await r.get("hello")
    if hello is None:
        await r.set("hello", "world")
        hello = "world"

    return {"hello": hello}

@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar(
    [index, get_book],
    openapi_config=OpenAPIConfig(
        title="Example API",
        description="This is an example API.",
        version="0.1.0",
        path="/docs",
        render_plugins=[StoplightRenderPlugin()]
    )
)
