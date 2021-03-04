from django.urls import path

from applications.lesson5.views import lesson5

urlpatterns = [
    path("", lesson5)
]