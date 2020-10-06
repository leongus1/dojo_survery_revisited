from django.shortcuts import render, HttpResponse

def index (request):
    # if request=="POST":
    #     context = request.POST
    #     return render (request, "display.html", context)
    # else:
    return render(request, "index.html")

def display(request):
    if request.method=="POST":
        context = {
            "first_name": request.POST['first_name'],
            "last_name": request.POST['last_name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'description': request.POST['description'],
            'gender': request.POST['gender'],
            'learned': request.POST['learned'],
            }
        return render (request, "display.html", context)
    
        
        

# Create your views here.
