from django.shortcuts import render

#Important
from .models import Project


def home(request):

    projects = Project.objects.all()
    # Add HTML from apps here
    return render(request, 'portfolio/home.html', {'projects':projects})
