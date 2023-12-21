from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
    )
from django.urls import reverse_lazy
from .models import TaskModel


class TaskListView(LoginRequiredMixin, ListView):
    """This class for display list of tasks"""

    model = TaskModel
    def get_context_data(self, **kwargs):
        """Return task list context which loggined user created tasks"""

        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False)

        search_input_data = self.request.GET.get("search-area")
        if search_input_data:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input_data) or ''

            context['search_input'] = search_input_data
        
        return context
    
    context_object_name = 'tasks'


class TaskDetailView(LoginRequiredMixin, DetailView):
    """This class for display task details each task"""

    model = TaskModel
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """This class for create a new task"""

    model = TaskModel
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        """Used for set atutomatically user when create task"""
        form.instance.user = self.request.user

        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """This class used for modify specific task"""

    model = TaskModel
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """This class used for remove specific task"""

    model = TaskModel
    success_url = reverse_lazy("tasks")
