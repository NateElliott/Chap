import json, requests, os
from .secf import load



class FBIO:

    token = load('fbkey')
    graph_url = 'https://graph.facebook.com'
    graph_version = 'v2.6'

    def __init__(self, payload):
        self.post_url = '{url}/{ver}/me/messages?access_token={token}'.format(url=self.graph_url,
                                                                                 ver=self.graph_version,
                                                                                 token=self.token)

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
        response_message = json.dumps({"recipient": {"id": self.sender_id}, "message": {"text": message}})
        response_headers = {"Content-Type": "application/json"}
        requests.post(self.post_url, headers=response_headers, data=response_message)

    def respond_image(self, file):
        header = {"Content-Type": "image/jpg"}
        data = json.dumps({
            "recipient": {"id": self.sender_id},
            "message": {"attachment": {"type":"image",
                                       "payload":""}}})

        #files = {'filedata': (file.filename, open(file, 'rb'), 'image/jpg')}
        #files = {"filedata": open(file,'rb')}

        print("gtg")

        #requests.post(self.post_url, data=data, headers=header, file=files)

    """



import requests
url = 'http://file.api.wechat.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
files = {'media': open('test.jpg', 'rb')}
requests.post(url, files=files)

curl  \
  -F 'recipient={"id":"USER_ID"}' \
  -F 'message={"attachment":{"type":"image", "payload":{}}}' \
  -F 'filedata=@/tmp/shirt.png;type=image/png' \
  "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"





    curl  \
      -F 'recipient={"id":"USER_ID"}' \
      -F 'message={"attachment":{"type":"image", "payload":{}}}' \
      -F 'filedata=@/tmp/shirt.png;type=image/png' \
      "https://graph.facebook.com/v2.6/me/messages?access_token=PAGE_ACCESS_TOKEN"

    """
    def raw(self):
        return self.payload_raw


    def __str__(self):
        return '{} {} - {}'.format(self.sender_first_name,self.sender_last_name, self.message_text)