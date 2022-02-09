import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from chatapp.routing import websockecturl
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(websockecturl)
    )
})