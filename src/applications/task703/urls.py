from django.urls import path

from applications.task703.views import task703

urlpatterns = [
    path("", task703)
]