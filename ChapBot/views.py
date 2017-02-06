from django.shortcuts import render
from django.views import View
from django.http import HttpResponse



from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json
import requests

# Create your views here.


def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAXUP705SWcBABV6CxKHG0Itm15YmZC4nEZC7lA1592qR1SPe8hk1srYfIEggSaIaNj5FBOQcjDPa1VPKoEzxP9wimVKcO6ob8CjHB2FfWpZCgzxPV65OJxcOkNL0HaA35NSS9tuQFNSfltmI6yFQ1deqGA2M09COPZBmHcyMwZDZD'
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)







class ChapBotView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ChapBotView, self).dispatch( request, *args, **kwargs)


    def get(self, request):

        if request.GET.get('hub.verify_token') == '4b4ac4dcf31c237ca31ad39cf719a664':
            return HttpResponse(request.GET['hub.challenge'])

        else:
            return HttpResponse('gtg')



    def post(self, request):

        message_payload = json.loads(request.body.decode('utf-8'))

        for entry in message_payload['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    message_text = message['message']['text']
                    message_sender_id = message['sender']['id']

                    post_facebook_message(message_sender_id,message_text)


        return HttpResponse('gtg')