# IMPORTS goes here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from copy import deepcopy


# GLOBAL VARs goes here.
guesstheword_keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],['A', 'S', 'D', 'F','G', 'H', 'J', 'K', 'L'],['Z', 'X', 'C', 'V', 'B', 'N', 'M']]


# VIEWS goes here.
class HomeView(generic.ListView):
    template_name = 'guesstheword/home.html'
    context_object_name = 'guesstheword'

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['keyboard'] = guesstheword_keyboard
        return context

