from django.urls import path
from users.api import views

urlpatterns = [
    path('', views.users, name='home'),

]