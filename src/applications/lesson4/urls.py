from django.urls import path

from applications.lesson4.views import Lesson4View

urlpatterns = [
    path("", Lesson4View.as_view())
]
