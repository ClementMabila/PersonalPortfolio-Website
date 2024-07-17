from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def academic_record(request):
    return render(request, 'portfolio/academic_record.html')

def projects(request):
    return render(request, 'portfolio/projects.html')