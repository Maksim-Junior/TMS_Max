from django.urls import path

from applications.lesson3.views import lesson3

urlpatterns = [
    path("", lesson3),
]
