from django.urls import path
from . import views

urlpatterns = [
        path('signup', views.CreateUserView.as_view(), name='sign_up'),
        path('users', views.UserView.as_view(), name='users'),

    ]