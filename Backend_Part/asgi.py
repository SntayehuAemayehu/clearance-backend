# Backend_Part/asgi.py
import os

# 🔥 THIS MUST BE BEFORE ALL DJANGO IMPORTS
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend_Part.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import api.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.routing.websocket_urlpatterns
        )
    ),
})