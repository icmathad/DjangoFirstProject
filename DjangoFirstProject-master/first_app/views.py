from django.shortcuts import render

# Create your views here.
from django.conf.urls import url

def index(request):
    value = {'insert_me': "Hello how are you"}
    return render(request, 'first_app/index.html', context=value)


def welcome(request):
    welcome = {'welcome': ' welcome from the views page'}
    return render(request, 'first_app/welcome.html', context=welcome)
