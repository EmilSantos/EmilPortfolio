from django.shortcuts import render, HttpResponse

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
  #return HttpResponse("This is my contact (/contact)")
  return render(request, 'contact.html')