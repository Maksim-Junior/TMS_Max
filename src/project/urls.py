from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("applications.index.urls")),
    path("b/", include("applications.blog.urls")),
    path("tasks/306/", include("applications.task306.urls")),
    path("tasks/307/", include("applications.task307.urls")),
    path("tasks/308/", include("applications.task308.urls")),
    path("tasks/310/", include("applications.task310.urls")),
    path("tasks/311/", include("applications.task311.urls")),
    path("tasks/402/", include("applications.task402.urls")),
    path("tasks/404/", include("applications.task404.urls")),
    path("tasks/406/", include("applications.task406.urls")),
    path("tasks/407/", include("applications.task407.urls")),
    path("tasks/501/", include("applications.task501.urls")),
    path("tasks/502/", include("applications.task502.urls")),
    path("tasks/503/", include("applications.task503.urls")),
    path("tasks/504/", include("applications.task504.urls")),
    path("tasks/507/", include("applications.task507.urls")),
    path("tasks/702/", include("applications.task702.urls")),
    path("tasks/703/", include("applications.task703.urls")),
]
