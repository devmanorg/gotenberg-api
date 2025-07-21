# Gotenberg API

Библиотека Gotenberg API упрощает работу с endpoint API для генерации скриншотов [gotenberg.dev](https://gotenberg.dev/docs/routes#screenshots-route), предоставляя тонкую обёртку над веб API и библиотекой HTTPX: добавляет к обычным возможностям HTTPX свои схемы данных, а также удобные, часто используемые функции, но не мешает, при необходимости, спускаться ниже на уровень HTTP-запросов.

## Использование

Библиотека использует асинхронный клиент.

Пример запроса:

```python
import httpx

from gotenberg_api import GotenbergServerError, ScreenshotHTMLRequest

 try:
    async with httpx.AsyncClient(base_url=settings_var.get().GOTENBERG_URL) as client:
        screenshot_bytes = await ScreenshotHTMLRequest(
            index_html=raw_html,
            width=1000,
        ).asend(client)
except GotenbergServerError as e:
    logger.error(e)
    screenshot_bytes = None
```

## Исключения

У библиотеки есть своё собственное исключение, которое через контекстный менеджер отлавливает исключение:

- [`httpx.HTTPError`](https://www.python-httpx.org/exceptions/)
