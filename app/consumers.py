import json
from channels.generic.websocket import WebsocketConsumer

class FirstConsumer(WebsocketConsumer):
    def connect(self):
        print('CONNECTED')
        self.accept()

    def disconnect(self, close_code):
        print('DISCONNECTED')
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("MESSAGE",message)
        self.send(text_data=json.dumps({
            'message': message
        }))