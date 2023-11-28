from django.urls import path, include, re_path
from .views import index, user

urlpatterns = [
    path('', index, name='home'),
   # re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', user)
    path('user/<str:name>/<int:age>', user, name='user')
]