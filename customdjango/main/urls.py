from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signin', login_attempts, name='signin'),
    path('signup', register_attempts, name='signup'),
    path('logout', login_attempts, name='logout'),
    path('profile/<int:pk>/', profiles, name='profile'),
]