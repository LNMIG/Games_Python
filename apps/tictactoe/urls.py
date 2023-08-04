from django.urls import path

from . import views


app_name = 'apps.tictactoe'

urlpatterns = [
    path('tictactoe/', views.HomeView.as_view(), name='home'),
    path('tictactoe/makemove/', views.makemove, name='makemove'),
    path('tictactoe/reset/', views.reset, name='resetgame'),
]