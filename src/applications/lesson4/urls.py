from django.urls import path

from applications.lesson4.views import lesson4

urlpatterns = [
    path("", lesson4)
]