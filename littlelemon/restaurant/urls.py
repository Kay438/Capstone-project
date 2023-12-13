from django.urls import path
from django.contrib import admin
from .views import sayHello

urlpatterns=[
    path('', sayHello, name="sayHello"),
]