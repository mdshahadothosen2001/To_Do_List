from django.shortcuts import render
from django.views.generic.list import ListView
from .models import StudyPlanModel


class StudyPlanView(ListView):
    """Used for display study plans"""

    model = StudyPlanModel
    context_object_name = "study_plans"
    


