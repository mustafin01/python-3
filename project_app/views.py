from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']
    path = request.path

    text = f' host: {host}, browser: {user_agent}, path: {path}, ip: {ip}'
    return HttpResponse(text)


def user(request, name='Noname', age=0):
    return HttpResponse(f'User: {name}. His age {age}')
