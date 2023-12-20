from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TaskModel


class TaskListView(ListView):
    """This class for display list of tasks"""

    model = TaskModel
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    """This class for display task details each task"""

    model = TaskModel
    context_object_name = 'task'


class TaskCreateView(CreateView):
    """This class for create a new task"""

    model = TaskModel
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdateView(UpdateView):
    """This class used for modify specific task"""

    model = TaskModel
    fields = "__all__"
    success_url = reverse_lazy("task")
