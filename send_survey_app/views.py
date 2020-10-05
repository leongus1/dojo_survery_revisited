from django.shortcuts import render, HttpResponse

def index (request):
    return HttpResponse("This route is working.")

# Create your views here.
