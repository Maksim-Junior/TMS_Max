from django.urls import path

from applications.task504.views import task504

urlpatterns = [
    path("", task504)
]