from django.shortcuts import render
from django.http import HttpResponse
from os import open

def index(request):
    return HttpResponse('This is a demo')

