from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
    )

urlpatterns = [
    #http://localhost:8000/task/
    path(route='', view=TaskListView.as_view(), name='tasks'),
    #http://localhost:8000/task/1/
    path(route="<int:pk>/", view=TaskDetailView.as_view(), name='task'),
    #http://localhost:8000/task/create/
    path(route="create/", view=TaskCreateView.as_view(), name="task_create"),
    #http://localhost:8000/task/update/1/
    path(route="update/<int:pk>/", view=TaskUpdateView.as_view(), name="task_update"),
    #http://localhost:8000/task/delete/1/
    path(route="delete/<int:pk>/", view=TaskDeleteView.as_view(), name="task_delete"),
]
