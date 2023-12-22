from django.urls import path
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView
    )



urlpatterns = [
    path(
        route="",
        view=NoteListView.as_view(),
        name="notes"
    ),
    path(
        route="detail/<int:pk>/",
        view=NoteDetailView.as_view(),
        name="note"
    ),
    path(
        route="create/",
        view=NoteCreateView.as_view(),
        name="note_create"
    ),
]
