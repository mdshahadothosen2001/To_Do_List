from django.contrib import admin
from .models import NoteModel


class NoteModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "description",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "user",
        "title",
        "description",
    )
    search_fields = (
        "user",
        "title",
    )
    list_per_page = 25


admin.site.register(NoteModel, NoteModelAdmin)
