from django.shortcuts import render, HttpResponse

# Create your views here.
def homeview(request, *args, **kwargs):
    return HttpResponse("Hello world")