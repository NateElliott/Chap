from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .helper import secf

from .helper.fbhelp import FBIO


class ChapBotView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ChapBotView, self).dispatch(request, *args, **kwargs)


    def get(self, request):
        if request.GET.get('hub.verify_token') == secf.load('rootkey'):
            return HttpResponse(request.GET['hub.challenge'])
        else:
            return HttpResponse('This is Chap')


    def post(self, request):

        payload = FBIO()
        payload.load(request.body.decode('utf-8'))

        if payload.is_message:
            payload.respond('Hi {}, this is Chap'.format(payload.sender_first_name))

        return HttpResponse('This is Chap.')
