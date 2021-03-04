from django.urls import path

from applications.task308.views import task308

urlpatterns = [
    path("", task308)
]