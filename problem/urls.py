from django.urls import path
from .views import problemList

app_name = 'problem'
urlpatterns = [
    path('', problemList, name='problemList'),

]