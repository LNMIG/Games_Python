import random


def read_data(filepath):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            word = line.split('|')[0].strip().upper()
            definition = line.split('|')[1].strip()
            word_definition = (word, definition)
            words.append(word_definition)
    return words


def run_main():
    data = read_data(filepath="./apps/guesstheword/dictionary.txt")
    chosen_tuple = random.choice(data)
    chosen_word = chosen_tuple[0]
    chosen_definition = chosen_tuple[1]
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}

    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    return (chosen_word_list, chosen_word_list_underscores,letter_index_dict, chosen_definition)