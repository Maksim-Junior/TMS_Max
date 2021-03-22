from django.urls import path

from applications.lesson7.views import Lesson7View

urlpatterns = [
    path("", Lesson7View.as_view())
]