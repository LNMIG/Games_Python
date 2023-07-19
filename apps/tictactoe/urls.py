from django.urls import path

from . import views


app_name = 'apps.tictactoe'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('makemove', views.makemove, name='makemove'),
]