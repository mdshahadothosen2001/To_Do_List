from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Used to view the home page where included task and other applications"""

    template_name = "home/home.html"
