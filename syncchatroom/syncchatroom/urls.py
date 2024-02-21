from django.urls import path, include
from django.contrib import admin  # Add this import statement
from .views import HomeView, RegistrationView, LoginView
from syncchat.routing import websocket_urlpatterns  # Import the WebSocket URL patterns

urlpatterns = [
    path('', HomeView.as_view(), name='message-list'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),  # Include the admin URLs
    path('ws/', include(websocket_urlpatterns)),
]
