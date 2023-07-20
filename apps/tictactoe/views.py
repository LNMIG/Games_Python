# IMPORTS goes here.
from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from copy import deepcopy

from .calculations import run


# GLOBAL VARs goes here.
tictactoe_initial = [['', '', ''],['', 'X', ''],['', '', '']]
tictactoe_final = []
tictactoe_winner = False
tictactoe_blocked = False


# VIEWS goes here.
class HomeView(generic.ListView):
    template_name = 'tictactoe/home.html'
    context_object_name = 'tictactoe'

    def get_queryset(self):
        if len(tictactoe_final)==0:
            return tictactoe_initial
        else:
            return tictactoe_final

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['blocked'] = tictactoe_blocked
        context['winner'] = tictactoe_winner
        return context


def makemove(request):
    # declare global vars to be accessed
    global tictactoe_final
    global tictactoe_initial
    global tictactoe_winner
    global tictactoe_blocked

    # get the user selection
    square_selected = request.POST['square']

    # check the selection is in range(0,8)
    if '0' <= square_selected <= '8':
        move = int(square_selected)
    else:
        move = 5

    # used when initializing game
    if len(tictactoe_final) == 0:
        result = run(deepcopy(tictactoe_initial), move)
    else:
        result = run(deepcopy(tictactoe_final), move)

    # used when someone/program wins or draw
    if result[1] != '':
        tictactoe_winner = result[1]
        tictactoe_blocked = True

    tictactoe_final = result[0]

    return HttpResponseRedirect(reverse('apps.tictactoe:home', args=()))

def reset(request):
    global tictactoe_final
    global tictactoe_winner
    global tictactoe_blocked

    tictactoe_final = []
    tictactoe_blocked = False
    tictactoe_winner = False

    return HttpResponseRedirect(reverse('apps.tictactoe:home', args=()))