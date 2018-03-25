# -*- coding: utf-8 -*-
from CAH import bot, w_cards, b_cards
from telebot import types

def new_round(game):
    bot.send_message(game.group_id, "La frase para esta ronda es:\n\n{}".format(b_cards[game.black_card].format('_____')))
    broadcast_cards(game)

def broadcast_cards(game):
    users_cards = game.get_cards()
    for uid, cards in users_cards.iteritems():
        keyboard = types.InlineKeyboardMarkup()
        for c in cards:
            keyboard.add(types.InlineKeyboardButton(w_cards[c], callback_data=str(c)))
        bot.send_message(uid, "La frase es:\n\n{}.\nElige una carta graciosa!".format(b_cards[game.black_card].format('_____')), reply_markup=keyboard)