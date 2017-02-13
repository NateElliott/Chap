import json, requests
from .secf import load


class FBIO:

    token = load('fbkey')
    graph_url = 'https://graph.facebook.com'
    graph_version = 'v2.6'

    def load(self, payload):

        self.payload_raw = payload
        self.payload = json.loads(self.payload_raw)

        for entry in self.payload['entry']:
            for message in entry['messaging']:

                if 'message' in message:
                    self.sender_id = message['sender']['id']
                    self.message_text = message['message']['text']
                    self.is_message = True
                    self.get_facebook_info()

                elif 'delivery' in message:
                    self.is_message = False

    def get_facebook_info(self):
        user_details_url = '{url}/{ver}/{fbid}'.format(url=self.graph_url,ver=self.graph_version,fbid=self.sender_id)
        user_details_params = {'fields': 'first_name,last_name', 'access_token': self.token}
        user_details = requests.get(user_details_url, user_details_params).json()

        self.sender_first_name = user_details['first_name']
        self.sender_last_name = user_details['last_name']


    def respond(self, message):
        post_message_url = '{url}/{ver}/me/messages?access_token={token}'.format(url=self.graph_url,
                                                                                 ver=self.graph_version,
                                                                                 token=self.token)
        response_message = json.dumps({"recipient": {"id": self.sender_id}, "message": {"text": message}})
        response_headers = {"Content-Type": "application/json"}
        requests.post(post_message_url, headers=response_headers, data=response_message)



