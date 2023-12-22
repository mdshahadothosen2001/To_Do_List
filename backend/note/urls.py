from django.urls import path
from .views import NoteListView



urlpatterns = [
    path(
        route="",
        view=NoteListView.as_view(),
        name="notes"
    ),
]
