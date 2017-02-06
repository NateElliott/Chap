from django.conf.urls import url
from ChapBot.views import ChapBotView



urlpatterns = [
    url(r'98df09bf76da3f97276c4db35165b172facaef5d2e0f4215fe', ChapBotView.as_view(), name='index')
]