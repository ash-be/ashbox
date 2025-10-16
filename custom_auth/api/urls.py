from django.urls import path
from custom_auth.api import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('refresh', views.create_access_by_rt, name='getATbyRT'),
]