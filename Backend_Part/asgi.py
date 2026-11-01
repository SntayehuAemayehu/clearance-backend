import os

# 1. Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend_Part.settings')

from django.core.asgi import get_asgi_application

# 2. Initialize Django FIRST. This populates the app registry.
django_asgi_app = get_asgi_application()

# 3. NOW it is safe to import your routing (which likely imports models)
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import api.routing

# 4. Finally, define the application
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.routing.websocket_urlpatterns
        )
    ),
})