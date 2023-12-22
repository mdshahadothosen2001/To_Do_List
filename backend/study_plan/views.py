from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import StudyPlanModel


class StudyPlanView(ListView):
    """Used for display study plans"""

    model = StudyPlanModel

    def get_context_data(self, **kwargs):
        """Return task list context which loggined user created tasks"""

        context = super().get_context_data(**kwargs)
        context['study_plans'] = context['study_plans'].filter(user=self.request.user)       
        return context
    context_object_name = "study_plans"


class StudyPlanCreateView(CreateView):
    """Used for make new study plan"""    

    model = StudyPlanModel
    fields = ["title", "start_time", "end_time", "work", "else_work", "priority"]
    success_url = reverse_lazy("study_plans")

    def form_valid(self, form):
        """Used for set user automatically"""

        form.instance.user = self.request.user
        return super().form_valid(form)