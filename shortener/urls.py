from django.urls import path
from .views import home  # Import the correct view

urlpatterns = [
    path('', home, name='shortener_home'),  # Ensure this name matches
]
