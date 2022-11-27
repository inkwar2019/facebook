from django.contrib import admin
from django.urls import path,include
from .views import first, second, create_user
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('first', first),
    path('second', second),
    path('create_user', csrf_exempt(never_cache(create_user))),
]
