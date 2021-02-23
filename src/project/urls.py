from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path

from main.pages import index
from tasks import tasks
from tasks.lesson3 import task306, lesson3, task307, task308, task310, task311
from tasks.lesson4 import lesson4, task402, task404, task406, task407
from tasks.lesson5 import lesson5, task501, task502, task503, task504, task507
from tasks.lesson7 import lesson7, task702, task703

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index.handler_django),
    path("tasks/", tasks.handler_django),
    path("tasks/lesson3/", lesson3.handler_django),
    path("tasks/lesson3/task306/", task306.handler_django),
    path("tasks/lesson3/task307/", task307.handler_django),
    path("tasks/lesson3/task308/", task308.handler_django),
    path("tasks/lesson3/task310/", task310.handler_django),
    path("tasks/lesson3/task311/", task311.handler_django),
    path("tasks/lesson4/", lesson4.handler_django),
    path("tasks/lesson4/task402/", csrf_exempt(task402.handler_django)),
    path("tasks/lesson4/task404/", task404.handler_django),
    path("tasks/lesson4/task406/", task406.handler_django),
    path("tasks/lesson4/task407/", task407.handler_django),
    path("tasks/lesson5/", lesson5.handler_django),
    path("tasks/lesson5/task501/", task501.handler_django),
    path("tasks/lesson5/task502/", task502.handler_django),
    path("tasks/lesson5/task503/", task503.handler_django),
    path("tasks/lesson5/task504/", task504.handler_django),
    path("tasks/lesson5/task507/", csrf_exempt(task507.handler_django)),
    path("tasks/lesson7/", lesson7.handler_django),
    path("tasks/lesson7/task702/", task702.handler_django),
    path("tasks/lesson7/task703/", task703.handler_django),
]
