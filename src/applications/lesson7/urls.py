from django.urls import path

from applications.lesson7.views import lesson7

urlpatterns = [
    path("", lesson7)
]