import json
from channels.generic.websocket import AsyncWebsocketConsumer

class UserChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_name = f'chat_{self.room_name}'
        self.user = self.scope['user'].username

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'user_joined',
                'notification': f'{self.user} has joined the chat'
            }
        )
        await self.accept()
    

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    
    async def disconnect(self, close_code):

        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'user_disconnected',
                'notification': f'{self.user} has left the chat'
            }
        )

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def user_joined(self, event):
        noti = event['notification']
        t = event['type']
        await self.send(text_data=json.dumps({
            'type': t,
            'notification': noti
        }))

    async def user_disconnected(self, event):
        noti = event['notification']
        t = event['type']
        await self.send(text_data=json.dumps({
            'type': t,
            'notification': noti
        }))


class GeneralChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = "general"
        self.group_name = f'room_{self.room_name}'
        self.user = self.scope['user'].username

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'user_joined',
                'notification': f'{self.user} has joined the chat'
            }
        )
        await self.accept()
    

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    
    async def disconnect(self, close_code):

        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'user_disconnected',
                'notification': f'{self.user} has left the chat'
            }
        )

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))


    async def user_joined(self, event):
        noti = event['notification']
        t = event['type']
        await self.send(text_data=json.dumps({
            'type': t,
            'notification': noti
        }))

    
    async def user_disconnected(self, event):
        noti = event['notification']
        t = event['type']
        await self.send(text_data=json.dumps({
            'type': t,
            'notification': noti
        }))


class ProgrammingChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = "programming"
        self.group_name = f'room_{self.room_name}'
        self.user = self.scope['user'].username

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'user_joined',
                'notification': f'{self.user} has joined the chat'
            }
        )
        await self.accept()
    

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    
    async def disconnect(self, close_code):

        await self.channel_layer.group_send(
            self.group_name,
            message={
                'type': 'user_disconnected',
                'notification': f'{user} has left the chat'
            }
        )

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))


    async def user_joined(self, event):
        noti = event['notification']
        t = event['type']
        await self.send(text_data=json.dumps({
            'type': t,
            'notification': noti
        }))


    async def user_disconnected(self, event):
        noti = event['notification']
        t = event['type']
        await self.send(text_data=json.dumps({
            'type': t,
            'notification': noti
        }))