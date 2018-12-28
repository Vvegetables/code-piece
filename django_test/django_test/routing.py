#coding=utf-8
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import websocket_chat_test.routing

application = ProtocolTypeRouter({
    #(http->django views is added by default
    "websocket" : AuthMiddlewareStack(
        URLRouter(
            websocket_chat_test.routing.websocket_urlpatterns
        )
    )
})