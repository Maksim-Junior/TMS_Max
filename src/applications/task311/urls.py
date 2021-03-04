from django.urls import path

from applications.task311.views import task311

urlpatterns = [
    path("", task311)
]