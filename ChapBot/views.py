import json, requests

from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .helper import sec


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

                    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={}'.format(sec.load('fbkey'))
                    response_msg = json.dumps({"recipient": {"id": message['sender']['id']}, "message": {"text": message['message']['text']}})
                    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)

                    return HttpResponse('gtg')


