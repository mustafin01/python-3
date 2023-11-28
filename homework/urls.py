from django.urls import path
from .views import index, error

urlpatterns = [
    path('', index, name='ip'),
    path('error/', error, name='error')
]




