from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.frontpage, name='frontpage'),
    path('signup/', views.signUpPage, name='signup'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]