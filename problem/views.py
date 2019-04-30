from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem
# Create your views here.


def problemList(request):
    problemList = Problem.objects.all()
    return HttpResponse(request, problemList)