from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
app_name="accounts"
urlpatterns = [
    path('profile', views.ProfileView.as_view(), name="profile"),

    #path('',TemplateView.as_view(template_name ='index.html'), name="index")

    #django authentication
    #accounts/login is one of the 8 django_auth configurations should be placed in as_views
    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),

]
