from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Problem
# Create your views here.


def problemList(request):
    problemList = Problem.objects.all()
    return render(request, 'problem/problemList.html', {'problemList':problemList})

def detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'problem/detail.html', {'problem': problem})
