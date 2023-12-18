from django.urls import path
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path(route='', view=TaskListView.as_view(), name='tasks'),
    path(route="task/<int:pk>/", view=TaskDetailView.as_view(), name='task'),
]
