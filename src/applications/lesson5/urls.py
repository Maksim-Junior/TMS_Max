from django.urls import path

from applications.lesson5.views import Lesson5View

urlpatterns = [
    path("", Lesson5View.as_view())
]