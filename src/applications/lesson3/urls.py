from django.urls import path

from applications.lesson3.views import Lesson3View

urlpatterns = [
    path("", Lesson3View.as_view()),
]
