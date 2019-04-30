from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.noticeList, name='noticeList'),
    path('<int:notice_id>/', views.detail, name='detail'),
]