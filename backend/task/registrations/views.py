from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View



class UserLoginView(LoginView):
    """This class used for login before task application"""

    fields = "__all__"
    template_name = "registrations/user_login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class CustomLogoutView(View):
    """This class used for logout before exists from task application"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('tasks'))
