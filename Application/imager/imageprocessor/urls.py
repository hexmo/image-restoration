from django.urls import path
from . import views


urlpatterns = [
    path('app', views.imageapp, name='app'),
    path('result', views.imageprocess, name='result')
]
