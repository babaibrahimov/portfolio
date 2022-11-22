from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def aboutMe(request):
    return render(request, 'about.html')

def social(request):
    return render(request, 'social.html')

def projects(request):
    return render(request, 'projects.html')