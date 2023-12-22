from django.views.generic.list import ListView
from .models import NoteModel



class NoteListView(ListView):
    """Used for display notes"""

    model = NoteModel
    context_object_name = "notes"
