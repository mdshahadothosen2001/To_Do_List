from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views import View



class UserCreationView(FormView):
    """This class used for user registration for task application"""

    template_name = "registrations/user_register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        """Used for check form data and save valid form"""

        user = form.save()

        if user is not None:
            login(self.request, user)

        return super(UserCreationView, self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        """Used for check user id authenticated then redirect"""

        if self.request.user.is_authenticated:
            return redirect('tasks')

        return super(UserCreationView, self).get(*args, **kwargs)


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
