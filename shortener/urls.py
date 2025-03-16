from django.urls import path
from .views import ShortenURL, RetrieveURL, UpdateURL, DeleteURL, URLStats,RedirectToOriginalURL

urlpatterns = [
    path('shorten/', ShortenURL.as_view(), name='shorten-url'),
    path('<str:short_code>/', RedirectToOriginalURL.as_view(), name='redirect-to-original-url'),
    path('shorten/<str:short_code>/', RetrieveURL.as_view(), name='retrieve-url'),
    path('shorten/<str:short_code>/update/', UpdateURL.as_view(), name='update-url'),
    path('shorten/<str:short_code>/delete/', DeleteURL.as_view(), name='delete-url'),
    path('shorten/<str:short_code>/stats/', URLStats.as_view(), name='url-stats'),
]