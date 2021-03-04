from django.urls import path

from applications.index.views import index

urlpatterns = [
    path("", index),
]
