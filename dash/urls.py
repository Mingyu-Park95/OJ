from django.urls import path
from dash.views import dash

app_name = 'dash'




urlpatterns = [
    path('', dash, name='dash'),
]