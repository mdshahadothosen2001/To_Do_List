from django.urls import path
from .views import TaskListView

urlpatterns = [
    path(route='',view=TaskListView.as_view(), name='tasks'),
]
