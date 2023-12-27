from django.urls import path
from .views import UserCreationView, UserLoginView, CustomLogoutView

urlpatterns = [
    # http://localhost:8000/user/register/
    path(route="register/", view=UserCreationView.as_view(), name="user_register"),
    # http://localhost:8000/user/login/
    path(route="login/", view=UserLoginView.as_view(), name="user_login"),
    # http://localhost:8000/user/logout/
    path(route="logout/", view=CustomLogoutView.as_view(), name="user_logout"),
]
