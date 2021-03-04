from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include

from tasks.lesson4 import task404, task406, task407
from tasks.lesson5 import lesson5, task501, task502, task503, task504, task507
from tasks.lesson7 import lesson7, task702, task703

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.index.urls")),
    path("tasks/", include("applications.tasks.urls")),
    path("tasks/lesson3/", include("applications.lesson3.urls")),
    path("tasks/lesson3/task306/", include("applications.task306.urls")),
    path("tasks/lesson3/task307/", include("applications.task307.urls")),
    path("tasks/lesson3/task308/", include("applications.task308.urls")),
    path("tasks/lesson3/task310/", include("applications.task310.urls")),
    path("tasks/lesson3/task311/", include("applications.task311.urls")),
    path("tasks/lesson4/", include("applications.lesson4.urls")),
    path("tasks/lesson4/task402/", include("applications.task402.urls")),
    path("tasks/lesson4/task404/", include("applications.task404.urls")),
    path("tasks/lesson4/task406/", include("applications.task406.urls")),
    path("tasks/lesson4/task407/", include("applications.task407.urls")),
    path("tasks/lesson5/", include("applications.lesson5.urls")),
    path("tasks/lesson5/task501/", include("applications.task501.urls")),
    path("tasks/lesson5/task502/", include("applications.task502.urls")),
    path("tasks/lesson5/task503/", include("applications.task503.urls")),
    path("tasks/lesson5/task504/", include("applications.task504.urls")),
    path("tasks/lesson5/task507/", include("applications.task507.urls")),
    path("tasks/lesson7/", include("applications.lesson7.urls")),
    path("tasks/lesson7/task702/", include("applications.task702.urls")),
    path("tasks/lesson7/task703/", include("applications.task703.urls")),
]
