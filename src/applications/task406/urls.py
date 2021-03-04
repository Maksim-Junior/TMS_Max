from django.urls import path

from applications.task406.views import task406

urlpatterns = [
    path("", task406)
]