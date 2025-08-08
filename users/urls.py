from django.urls import path
from .views.regitser import RegisterView
from .views.login import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]