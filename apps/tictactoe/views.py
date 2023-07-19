from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

tictactoe_initial = ['', '', '', '', 'X', '', '', '', '']
tictactoe_final = []

# Create your views here.
class HomeView(generic.ListView):
    # global tictactoe_initial
    # global tictactoe_final


    template_name = 'tictactoe/home.html'
    context_object_name = 'tictactoe'
    
    def get_queryset(self):
        print(self.request)
        print(tictactoe_initial)
        print(tictactoe_final)
        
        if len(tictactoe_final)==0:
            return tictactoe_initial
        else:
            return tictactoe_final

def makemove(request):
    global tictactoe_final
    tictactoe_final = ['X', '', '', '', 'X', '', '', '', 'X']
    square_selected = request.POST['square']
    print(square_selected)
    print(tictactoe_final)
    return HttpResponseRedirect(reverse('apps.tictactoe:home', args=()))