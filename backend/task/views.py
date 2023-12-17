from django.views.generic.list import ListView
from .models import TaskModel


class TaskListView(ListView):
    model = TaskModel
    context_object_name = 'tasks'
