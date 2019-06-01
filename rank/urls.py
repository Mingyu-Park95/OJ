from django.urls import path

from rank.views import rank

app_name = 'rank'
urlpatterns = [
    path('',rank, name='rank'),

]