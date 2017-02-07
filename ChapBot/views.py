import json, requests

from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .helper import secf
from .helper import fbhelp

class ChapBotView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ChapBotView, self).dispatch( request, *args, **kwargs)

    def get(self, request):
        if request.GET.get('hub.verify_token') == secf.load('rootkey'):
            return HttpResponse(request.GET['hub.challenge'])
        else:
            return HttpResponse('gtg')

    def post(self, request):
        msg = fbhelp.read_facebook_message(request.body.decode('utf-8'))
        fbhelp.send_facebook_message(msg['fbid'], msg['message'])

        return HttpResponse()


