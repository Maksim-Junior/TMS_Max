from django.urls import path

from applications.task503.views import task503

urlpatterns = [
    path("", task503)
]