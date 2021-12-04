from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
  #return HttpResponse("This is my homepage (/)")
  context = {'name': "Emil", 'course': 'Django'}
  return render(request, 'home.html', context)

def about(request):
  #return HttpResponse("This is my about (/about)")
  return render(request, 'about.html')

def projects(request):
  #return HttpResponse("This is my projects (/projects)")
  return render(request, 'projects.html')

def contact(request):
  if request.method=="POST":
    print("This is post")
    name = request.POST["name"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    desc = request.POST["desc"]
    print(name, email, phone, desc)
    contact = Contact(name=name, email=email, phone=phone, desc=desc)
    contact.save()
    print("the data has been written to the db")

  #return HttpResponse("This is my contact (/contact)")
  return render(request, 'contact.html')