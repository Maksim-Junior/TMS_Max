from django.urls import path

from applications.task404.views import task404

urlpatterns = [
    path("", task404)
]
