from django.urls import path

from applications.task407.views import task407

urlpatterns = [
    path("", task407)
]