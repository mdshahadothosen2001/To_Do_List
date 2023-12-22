from django.urls import path
from .views import StudyPlanView

urlpatterns = [
    path(
        route="",
        view=StudyPlanView.as_view(),
        name="study_plans"
    ),
]
