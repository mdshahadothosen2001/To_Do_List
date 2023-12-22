from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import NoteModel



class NoteListView(ListView):
    """Used for display notes"""

    model = NoteModel
    context_object_name = "notes"


class NoteDetailView(DetailView):
    """Used to read note"""

    model = NoteModel
    context_object_name = "note"
