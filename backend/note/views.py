from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import NoteModel


class NoteListView(ListView):
    """Used for display notes"""

    model = NoteModel

    def get_context_data(self, **kwargs):
        """Return task list context which loggined user created tasks"""

        context = super().get_context_data(**kwargs)
        context["notes"] = context["notes"].filter(user=self.request.user)
        return context

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


class NoteDeleteView(DeleteView):
    """Used for delete specific note"""

    model = NoteModel
    success_url = reverse_lazy("notes")


class NoteUpdateView(UpdateView):
    """Used for update note"""

    model = NoteModel
    fields = ["title", "description"]
    success_url = reverse_lazy("notes")
