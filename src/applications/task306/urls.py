from django.urls import path

from applications.task306.views import task306

urlpatterns = [
    path("", task306)
]