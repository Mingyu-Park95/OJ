from django.urls import path
from .views import problemList, detail

app_name = 'problem'
urlpatterns = [
    path('', problemList, name='problemList'),
    path('<int:problem_id>', detail, name='detail'),

]