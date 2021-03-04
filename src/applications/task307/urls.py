from django.urls import path

from applications.task307.views import task307

urlpatterns = [
    path("", task307)
]