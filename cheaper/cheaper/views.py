from time import sleep

from django.http import HttpResponse
from django.views import View


class TestView(View):

    def get(self, request):
        sleep(2)
        return HttpResponse('OK')
