from django.urls import path

from authorization.views import RegisterUser, LoginUser, logout_user, home_view
urlpatterns = [
    path('register/',  RegisterUser.as_view(), name='register'),
    path('login/',  LoginUser.as_view(), name='login'),
    path('logout/',  logout_user, name='logout'),
    path('',  home_view, name='home'),


]