from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Messages
from asgiref.sync import sync_to_async

class ConsumerServer(AsyncWebsocketConsumer):
    
    # to accept the connection from the client
    async def connect(self):
        await self.channel_layer.group_add('Philosophy', self.channel_name)
        print(self.scope['user'])
        await self.accept()
        
    # broadcasting to the group
    async def  receive(self, text_data):
        user= self.scope["user"]
        user_img_url= await sync_to_async(self.get_user_img_url)(user)
        message= json.loads(text_data)
        print(message)
        if message:
            await sync_to_async(self.save_messages)(tdata=message["message"], sender=self.scope.get('user'))
            await self.channel_layer.group_send('Philosophy',{'type': 'main.rcv',
            "message" : message['message'],'user':user.username, 'image': user_img_url })
            # print(text_data)

    # method used by the channel layer group broadcast in its 'type key' and used to send back to the websocket client
    async def  main_rcv(self, event):
        if event.get('user') == self.scope['user'].username:
            print(event['user'])
            await self.send(text_data=json.dumps({'message':event['message'], 'user':event['user'], 'image':event['image']}))


    async def disconnect(self, code):
        await self.channel_layer.group_discard('Philosophy', self.channel_name)
        return await super().disconnect(code)

    # save user interactions into the data base.
    def save_messages(self, tdata, sender):
        msg= Messages(sender=sender, room_messages=tdata)
        msg.save()
        return msg
    # a function to get the profile image url of the user sending a message, to enable image display in chat
    def get_user_img_url(self,user):
        url= user.userprofile.image.url
        return url