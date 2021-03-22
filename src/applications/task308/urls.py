from django.urls import path

from applications.task308.views import Task308View

urlpatterns = [
    path("", Task308View.as_view())
]
