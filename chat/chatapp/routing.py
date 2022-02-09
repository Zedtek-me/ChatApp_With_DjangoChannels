from django.conf.urls import url
from .consumer import ConsumerServer

websockecturl=[
    url(r'^chat/$', ConsumerServer.as_asgi() )
]