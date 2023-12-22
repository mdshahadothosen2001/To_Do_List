from django.db import models
from django.contrib.auth.models import User


class StudyPlanModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    title = models.CharField(max_length=100, null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    work = models.CharField(max_length=100, null=True, blank=True)
    else_work = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']
        verbose_name = "Study_Plan"
        verbose_name_plural = "Study_plans"
        db_table = "study_plan"
