from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    text = f' host: {host}, browser: {user_agent}, path: {path}'
    return HttpResponse(text)


def error(request):
    return HttpResponse('Произошла ошибка <br>status: 400', status=400, reason='Incorrect data')