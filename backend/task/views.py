from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TaskModel


class TaskListView(ListView):
    """This class for display list of tasks"""

    model = TaskModel
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    """This class for display task details each task"""

    model = TaskModel
    context_object_name = 'task'
