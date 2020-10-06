from django.shortcuts import render, redirect

def index (request):
    if request.method =="POST":
        print('redirected')
        return render (request, "display.html")
    else:
        return render(request, "index.html")

def display(request):
    if request.method=="POST":
        request.session["first_name"]= request.POST['first_name']
        request.session['last_name']= request.POST['last_name']
        request.session['location']= request.POST['location']
        request.session['language']= request.POST['language']
        request.session['gender']= request.POST['gender']
        request.session['learned']= request.POST['learned']
        request.session['description']= request.POST['description']
        return redirect('../result/')
    else:
        print('redirected')
        return render (request, "display.html")
    
        
        

# Create your views here.
