from email import message
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Messages
from asgiref.sync import sync_to_async

class ConsumerServer(AsyncWebsocketConsumer):

    # to accept the connection from the client
    async def connect(self):
        await self.channel_layer.group_add('Philosophy', self.channel_name)
        await self.accept()
        
    # broadcasting to the group
   

    async def main_rcv(self, event):
        await sync_to_async(self.save_messages)(tdata=event, sender=self.scope.get('user'))
        await self.channel_layer.group_send('Philosophy',{'type': 'self.receive',
        "message" : event})
        # print(text_data)

    # method used by the group broadcasting method in its 'type key' and used to send back to the client 
    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data)


    async def disconnect(self, code):
        await self.channel_layer.group_discard('Philosophy', self.channel_name)
        return await super().disconnect(code)

    def save_messages(self, tdata, sender):
        msg= Messages(sender=sender, room_messages=tdata)
        msg.save()
        return msg