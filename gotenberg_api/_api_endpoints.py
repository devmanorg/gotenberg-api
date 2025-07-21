from typing import Literal

import httpx
from pydantic import BaseModel, ConfigDict

from ._exceptions import GotenbergServerError

request_schema_config = ConfigDict(
    extra='forbid',
    str_strip_whitespace=True,
    use_attribute_docstrings=True,
    validate_default=True,
    validate_assignment=True,
    validate_by_name=True,
    validate_by_alias=True,
)


class ScreenshotHTMLRequest(BaseModel):
    index_html: str
    width: int
    """Width to resize screen to before screenshot making. Pixels number."""
    format: Literal["png", "jpeg", "webp"] = "jpeg"

    model_config = request_schema_config

    async def asend(self, httpx_gotenberg_async_client: httpx.AsyncClient) -> bytes:
        async with GotenbergServerError.async_reraise_from(httpx.HTTPError):
            response = await httpx_gotenberg_async_client.post(
                "/forms/chromium/screenshot/html",
                files={
                    "files": ("index.html", self.index_html),
                    "width": (None, str(self.width)),
                    "format": (None, self.format),
                    "skipNetworkIdleEvent ": (None, "false"),
                    "waitForExpression": (None, "document.readyState === 'complete'"),
                },
            )
            response.raise_for_status()
            return await response.aread()
