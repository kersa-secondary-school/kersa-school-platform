# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f"user_{self.scope['user'].id}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        receiver_id = data['receiver_id']
        message = data['message']
        # save to database
        await self.channel_layer.group_send(
            f"user_{receiver_id}",
            {'type': 'chat_message', 'message': message, 'sender': self.scope['user'].username}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))