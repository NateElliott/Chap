import json, requests
from .secf import load


def send_facebook_message(fbid,message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={}'.format(load('fbkey'))
    response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    return status

def read_facebook_message(payload):
    message_payload = json.loads(payload)
    for entry in message_payload['entry']:
        for message in entry['messaging']:
            if 'message' in message:
                return {'fbid':message['sender']['id'], 'message': message['message']['text']}

