from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'socket.io/', consumers.FirstConsumer.as_asgi()),
    re_path(r'ws/chat//$', consumers.FirstConsumer.as_asgi())
]