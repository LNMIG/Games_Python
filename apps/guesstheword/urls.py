from django.urls import path

from . import views


app_name = 'apps.guesstheword'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('makemove', views.makemove, name='makemove'),
    # path('reset', views.reset, name='resetgame'),
]