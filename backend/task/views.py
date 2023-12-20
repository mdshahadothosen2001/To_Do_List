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
    context_object_name = 'tasks'


class TaskDetailView(LoginRequiredMixin, DetailView):
    """This class for display task details each task"""

    model = TaskModel
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """This class for create a new task"""

    model = TaskModel
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """This class used for modify specific task"""

    model = TaskModel
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """This class used for remove specific task"""

    model = TaskModel
    success_url = reverse_lazy("tasks")
