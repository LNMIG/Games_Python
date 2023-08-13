from django.urls import path

from . import views


app_name = 'apps.guesstheword'

urlpatterns = [
    path('guesstheword/', views.HomeView.as_view(), name='home'),
]