from django.shortcuts import render

def dash(request):
    return render(request, 'dash/dash.html')

# Create your views here.
