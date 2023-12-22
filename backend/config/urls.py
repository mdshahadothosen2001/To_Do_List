from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("task/", include("task.urls")),
    path("user/", include("task.registrations.urls")),
    path("", include("home.urls")),
    path("study-plan/", include("study_plan.urls")),
    path("note/", include("note.urls"),)
]
