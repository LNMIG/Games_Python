# IMPORTS goes here.
from django.urls import reverse
from django.views import generic

from .keyboard import keyboard_keys
from .main import run_main


# GLOBAL VARs goes here.
chosen_word_list = ''
letter_index_dict = ''
chosen_word_list_underscores = ''
keyboard = ''


# VIEWS goes here.
class HomeView(generic.ListView):
    template_name = 'guesstheword/home.html'

    def get_queryset(self):
        global chosen_word_list
        global letter_index_dict
        global chosen_word_list_underscores
        global keyboard

        chosen_parameters = run_main()
        chosen_word_list = chosen_parameters[0] if not chosen_word_list else chosen_word_list
        print('Estoy en queryset 1',chosen_word_list)
        letter_index_dict = chosen_parameters[2] if not letter_index_dict else letter_index_dict
        chosen_word_list_underscores = chosen_parameters[1] if not chosen_word_list_underscores else chosen_word_list_underscores
        keyboard = keyboard_keys()
        return chosen_word_list_underscores

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['guesstheword'] = chosen_word_list_underscores
        context['keyboard'] = keyboard
        return context
    
    def reset_global_variables(self):
        global chosen_word_list
        global letter_index_dict
        global chosen_word_list_underscores
        global keyboard

        chosen_word_list = ''
        letter_index_dict = ''
        chosen_word_list_underscores = ''
        keyboard = ''

    def post(self, request, *args, **kwargs):
        # get the user selection
        key_selected = request.POST['key']

        # create an object_list for HomeView
        self.object_list = chosen_word_list_underscores

        # get the context
        context = super().get_context_data(**kwargs)

        # check if the game should be reseted
        if key_selected == "RESET THE GAME":
            self.reset_global_variables()
            self.get_queryset()

        # check if the selected key=letter is in chosen word
        if key_selected in chosen_word_list:
            for idx in letter_index_dict[key_selected]:
                chosen_word_list_underscores[idx] = key_selected

        if "_" not in chosen_word_list_underscores:
            context['guesstheword'] = chosen_word_list_underscores
            context['keyboard'] = keyboard
            context['solved'] = 'Well done! You guessed the word!'
        else:
            context['guesstheword'] = chosen_word_list_underscores
            context['keyboard'] = keyboard

        return self.render_to_response(context)