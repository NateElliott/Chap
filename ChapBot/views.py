from django.views import View
from django.http import HttpResponse


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from .models import Contacts, Messages
from .helper import secf
from .helper.fbhelp import FBIO
from .helper.camcapture import CamCapture


class ChapBotView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ChapBotView, self).dispatch(request, *args, **kwargs)


    def get(self, request):
        if request.GET.get('hub.verify_token') == secf.load('rootkey'):
            return HttpResponse(request.GET['hub.challenge'])
        else:
            return HttpResponse('Hello, this is Chap.')


    def post(self, request):

        payload = FBIO(request.body.decode('utf-8'))

        if payload.is_message:

            try:
                # current user, eval
                user = Contacts.objects.get(fbid=payload.sender_id)

            except ObjectDoesNotExist:

                # new user, onboard
                user = Contacts(fbid=payload.sender_id,
                        first_name=payload.sender_first_name,
                        last_name=payload.sender_last_name).save()


            abc = CamCapture('test.jpg')

            payload.respond('Hey {}, how are you today? :)'.format(payload.sender_first_name))

            payload.respond_image(abc)


            Messages(user=user,message=payload.message_text).save()





        return HttpResponse('Hello, this is Chap.')
