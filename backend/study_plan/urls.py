from django.urls import path
from .views import (
    StudyPlanView,
    StudyPlanCreateView,
    StudyPlanDeleteView
    )

urlpatterns = [
    path(
        route="",
        view=StudyPlanView.as_view(),
        name="study_plans"
    ),
    path(
        route="create/",
        view=StudyPlanCreateView.as_view(),
        name="study_plan_create"
    ),
    path(
        route="delete/<int:pk>/",
        view=StudyPlanDeleteView.as_view(),
        name="study_plan_delete"
    ),
]
