from django.urls import path
from .views import HomePageView


urlpatterns = [
    path(route="", view=HomePageView.as_view(), name="home"),
]

