from django.urls import path
from django.contrib.auth import views as auth_view
from .views import register


urlpatterns = [
    # 로그인 검사 해주는 뷰. 실패하면 통과 못하고 성공하면 setting.py의  LOGIN_REDIRECT_URL에 따라 작동
    path('', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
