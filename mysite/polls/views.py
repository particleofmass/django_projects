from django.shortcuts import render
from django.http import HttpResponse
from os import open

def pollspolls(request):
    return HttpResponse('This is pollspolls')
def polls(request):
    return HttpResponse('this is the polls page')
def mainpage(request):
    return HttpResponse('This is the main page')
