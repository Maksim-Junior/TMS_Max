from django.urls import path

from applications.task311.views import Task311View

urlpatterns = [
    path("", Task311View.as_view())
]
