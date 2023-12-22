from django.contrib import admin
from .models import StudyPlanModel


class StudyPlanModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "start_time",
        "end_time",
        "work",
        "else_work",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "user",
        "title",
        "work",
        "else_work",
    )
    search_fields = (
        "user",
        "title",
    )
    list_per_page = 25

admin.site.register(StudyPlanModel, StudyPlanModelAdmin)
