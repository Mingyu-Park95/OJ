from django.urls import path
from .views import problemList, detail, check, code

app_name = 'problem'
urlpatterns = [
    path('', problemList, name='problemList'),
    path('<int:problem_id>', detail, name='detail'),
    path('check<int:problem_id>', check, name ='check'),
    path('code<int:code_id>', code, name='code'),
]