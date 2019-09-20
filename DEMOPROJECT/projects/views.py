from django.http import Http404
from django.shortcuts import render
from .models import Computer_Science

def index(request):
    all_projects = Computer_Science.objects.all()
    return render(request,'projects/index.html' , {'all_projects': all_projects} )


def details(request, student_id):
    try:
        Project_Name = Computer_Science.objects.get(pk= student_id)
    except Computer_Science.DoesNotExist:
        raise Http404("Student Data Dose Not Exist")
    return render(request, 'projects/detail.html', {'Project_Name': Project_Name})
