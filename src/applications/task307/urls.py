from django.urls import path

from applications.task307.views import Task307View

urlpatterns = [
    path("", Task307View.as_view())
]
