from django.urls import path

from applications.tasks.views import tasks

urlpatterns = [
    path("", tasks),
]
