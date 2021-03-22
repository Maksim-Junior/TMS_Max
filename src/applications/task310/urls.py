from django.urls import path

from applications.task310.views import Task310View

urlpatterns = [
    path("", Task310View.as_view())
]