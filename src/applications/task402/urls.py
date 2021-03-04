from django.urls import path

from applications.task402.views import task402

urlpatterns = [
    path("", task402)
]