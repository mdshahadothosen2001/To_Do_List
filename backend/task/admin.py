from django.contrib import admin
from .models import TaskModel


class TaskModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "description",
        "complete",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "user",
        "title",
    )
    search_fields = (
        "user",
        "title",
    )


admin.site.register(TaskModel, TaskModelAdmin)
