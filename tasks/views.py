from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def server(req):
    return HttpResponse('helloworld 😀')