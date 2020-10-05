from django.shortcuts import render, HttpResponse

def index (request):
    return render(request, "index.html")

def display(request):
    if request=="POST":
        context = request.POST
    return render (request, "display.html", context)
    
        
        

# Create your views here.
