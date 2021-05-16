from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('privacy', views.privacy, name='privacy')]
