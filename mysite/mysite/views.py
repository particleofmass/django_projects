from django.http import HttpResponse

def mainpage(request):
    return HttpResponse('This is the main page')
