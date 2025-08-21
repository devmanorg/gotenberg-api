# Gotenberg API

Библиотека Gotenberg API упрощает работу с endpoint API для генерации скриншотов [gotenberg.dev](https://gotenberg.dev/docs/routes#screenshots-route), предоставляя тонкую обёртку над веб API и библиотекой [HTTPX](https://www.python-httpx.org/).

Она добавляет к обычным возможностям [HTTPX](https://www.python-httpx.org/) свои схемы данных, а также удобные, часто используемые функции, но не мешает, при необходимости, спускаться ниже на уровень HTTP-запросов.

## Установка

Вы можете установить библиотеку с помощью `pip`:
```shell
# Установить из публичного GitHub репозитория (рекомендуемый способ)
$ pip install git+https://github.com/devmanorg/gotenberg-api.git

# Установить из приватного GitLab репозитория (если у вас есть к нему доступ)
$ pip install git+https://gitlab.dvmn.org/dvmn/courses/fastapi/gotenberg-api.git
```

## Использование

Библиотека использует [асинхронный HTTPX клиент](https://www.python-httpx.org/api/#asyncclient).

Для запуска требуется указать следующие настройки:

- `httpx.AsyncClient.base_url` - базовый адрес [Gotenberg API](https://gotenberg.dev/docs/getting-started/installation#live-demo-). Обязательная настройка.
- `ScreenshotHTMLRequest.width` - ширина скриншота в пикселях. Обязательная настройка.
- `ScreenshotHTMLRequest.format` - формат скриншота (может принимать значения `jpeg`, `png`, `webp`). По-умолчанию - `jpeg`.
- `ScreenshotHTMLRequest.wait_delay` - время ожидания завершения анимаций на html-странице. По-умолчанию - 2 секунды.
- опциональные настройки [асинхронного клиента](https://www.python-httpx.org/api/#asyncclient)

**Важно:** время ожидания завершения анимаций должно быть меньше таймаута [асинхронного клиента](https://www.python-httpx.org/api/#asyncclient), иначе библиотека всегда будет возвращать `TimeoutError`.  
Рекомендуемая разница между временем ожидания и таймаутом составляет **от 2 до 5 секунд**.

Пример запроса:

```python
import httpx

from gotenberg_api import GotenbergServerError, ScreenshotHTMLRequest

 try:
    async with httpx.AsyncClient(
        base_url=settings_var.get().GOTENBERG_URL,
        timeout=15,
    ) as client:
        screenshot_bytes = await ScreenshotHTMLRequest(
            index_html=raw_html,
            width=1000,
            format='png',
            wait_delay=5,
        ).asend(client)
except GotenbergServerError as e:
    logger.error(e)
    screenshot_bytes = None
```

## Исключения

У библиотеки есть своё собственное исключение, которое через контекстный менеджер отлавливает исключение:

- [`httpx.HTTPError`](https://www.python-httpx.org/exceptions/)
