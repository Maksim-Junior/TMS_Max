from django.urls import path

from applications.task502.views import task502

urlpatterns = [
    path("", task502)
]