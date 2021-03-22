from django.urls import path

from applications.task306.views import Task306View

urlpatterns = [
    path("", Task306View.as_view())
]