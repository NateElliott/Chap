import json, requests
from .secf import load


class FBIO:

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={}'.format(load('fbkey'))


    def load(self, payload):
        self.payload_raw = payload
        self.payload = json.loads(self.payload_raw)
        for entry in self.payload['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    self.sender_id = message['sender']['id']
                    self.message_text = message['message']['text']
                    self.is_message = True
                elif 'delivery' in message:
                    self.is_message = False

    def respond(self, message):
        response_message = json.dumps({"recipient": {"id": self.sender_id}, "message": {"text": message}})
        response_headers = {"Content-Type": "application/json"}
        requests.post(self.post_message_url, headers=response_headers, data=response_message)

