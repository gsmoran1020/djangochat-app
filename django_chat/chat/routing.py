from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.UserChatConsumer.as_asgi()),
    re_path(r'ws/chat/general/', consumers.GeneralChatConsumer.as_asgi()),
    re_path(r'ws/chat/programming/', consumers.ProgrammingChatConsumer.as_asgi()),
]