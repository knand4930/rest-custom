from django.urls import *
from .views import *

urlpatterns =[
    path('register/', ResgisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/<int:pk>', UserUpdate.as_view(), name='update'),
]
