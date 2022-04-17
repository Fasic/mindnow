from django.urls import path, include
from django.contrib.auth import views as views_auth
from mind_auth.views import RegistrationView

app_name = 'mind_auth'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', views_auth.LoginView.as_view(), name='login'),
    path('logout/', views_auth.LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
]
