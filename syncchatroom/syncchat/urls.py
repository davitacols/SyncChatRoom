# syncchat/urls.py

from django.urls import path
from .views import HomeView, MessageListView, RegistrationView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
