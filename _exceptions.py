from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager


class GotenbergServerError(Exception):

    @classmethod
    @asynccontextmanager
    async def async_reraise_from(
        cls,
        *exc: type[Exception],
        msg: str = "Gotenberg server error",
    ) -> AsyncGenerator[None]:
        try:
            yield
        except exc as e:
            raise cls(f"{msg}: {e!r}") from e
