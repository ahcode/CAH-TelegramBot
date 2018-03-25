# -*- coding: utf-8 -*-
from config import cards_language

def load_cards():
    w_file = open('cards/' + cards_language + '/white_cards.txt', 'r')
    white_cards = w_file.read().splitlines()
    w_file.close()
    b_file = open('cards/' + cards_language + '/black_cards.txt', 'r')
    black_cards = b_file.read().splitlines()
    b_file.close
    return (len(white_cards), len(black_cards), white_cards, black_cards)