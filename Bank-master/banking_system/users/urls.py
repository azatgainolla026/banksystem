from django.urls import path
from . import views
from .views import register_view, login_view, logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path("profile/", views.profile, name="profile"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
