from django.urls import path

from applications.task507.views import task507

urlpatterns = [
    path("", task507)
]