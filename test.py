from litestar import Litestar, get
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import StoplightRenderPlugin


@get("/")
async def index() -> dict[str, str]:
    return {"response": "ok"}


@get("/book")
async def index() -> dict[str, str]:
    return {"response": "ok"}


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
