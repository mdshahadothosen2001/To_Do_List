from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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


class NoteCreateView(CreateView):
    """Used for make new note"""

    model = NoteModel
    fields = ["title", "description"]
    def form_valid(self, form):
        """Used for set user automatically"""

        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy("notes")
