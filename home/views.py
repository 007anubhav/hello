from django.shortcuts import render,HttpResponse
from home.models import Contact 
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    context = {
        "variable1":"anubhav is great",
        "variable2":"anubhav is great"
    }
    return render(request, 'index.html',context)
    
def about(request):
   # return HttpResponse("this is about page")
    return render(request, 'about.html',)

def services(request):
    #return HttpResponse("this is services page")
    return render(request, 'services.html',)

def contact(request):
    #return HttpResponse("this is contact page")
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
        contact.save()
    messages.success(request, 'your message has been sent') 
    return render(request, 'contact.html',)