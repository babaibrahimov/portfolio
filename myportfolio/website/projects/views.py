from django.shortcuts import render, redirect
from .models import Projects

# Create your views here.
def project(request):
    form = Projects()
    objects = Projects.objects.all()
    if request.GET.get('q'):
        q = request.GET.get('q')
        objects = Projects.objects.filter(name__contains=q)

        
    context = {
        "form": form,
        "objects_list": objects
    }
    return render(request, 'projects.html', context)


# def projectDetail(request, pk):
#     project = Projects.objects.get(pk=pk)
#     context = {
#         'project': project
#     }
#     return render(request, 'project_detail.html', context)


def projectDetail(request,id):
    projects = Projects.objects.get(id=id)
    return render(request, 'project_detail.html', {"projects":projects})


def addproject(request):
    if request.method=="POST":
        req=request.POST
        name, date, responsive = req['name'], req['date'], req.get('responsive', False)
        if responsive == 'on':
            responsive = True
        img = request.FILES['img']
        print(responsive)
        newProject = Projects(name=name, responsive=responsive,  image=img, date=date)
        newProject.save()
        return redirect('home')
    return render(request, 'add_project.html')