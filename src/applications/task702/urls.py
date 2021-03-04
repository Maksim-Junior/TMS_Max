from django.urls import path

from applications.task702.views import task702

urlpatterns = [
    path("", task702)
]