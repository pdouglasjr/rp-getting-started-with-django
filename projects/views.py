from django.shortcuts import render
from projects.models import Project

def project_index(request):
    # Grab all projects from DB
    projects = Project.objects.all()

    # Create data context to pass back to requestor
    context = {
        'projects': projects
    }

    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    # Grab the requested project from DB
    project = Project.objects.get(pk=pk)

    # Create data context to pass back to requestor
    context = {
        'project': project
    }

    return render(request, 'projects/project_detail.html', context)