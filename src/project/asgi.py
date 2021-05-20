"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

_application = get_asgi_application()


async def application(scope, receive, send):
    if scope["path"].startswith("/api"):
        from api.asgi import app

        return await app(scope, receive, send)
    else:
        return await _application(scope, receive, send)
