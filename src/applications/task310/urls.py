from django.urls import path

from applications.task310.views import task310

urlpatterns = [
    path("", task310)
]