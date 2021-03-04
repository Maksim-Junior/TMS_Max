from django.urls import path

from applications.task501.views import task501

urlpatterns = [
    path("", task501)
]
