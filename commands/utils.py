# -*- coding: utf-8 -*-
from CAH import bot, w_cards, b_cards, users, games
from telebot import types
from config import self_voting

def new_round(game):
    game.new_round()
    bot.send_message(game.group_id, "La frase para esta ronda es:\n\n{}".format(b_cards[game.black_card].format('_____')))
    users_cards = game.get_cards()
    for uid, cards in users_cards.iteritems():
        keyboard = types.InlineKeyboardMarkup()
        for c in cards:
            keyboard.add(types.InlineKeyboardButton(w_cards[c], callback_data=str(c)))
        bot.send_message(uid, "La frase es:\n\n{}.\nElige una carta graciosa!".format(b_cards[game.black_card].format('_____')), reply_markup=keyboard)

def start_game(game):
    if game.start():
        bot.send_message(game.group_id, "Por fin! La partida acaba de empezar!")
        new_round(game)
    else:
        bot.send_message(game.group_id, "No hay suficientes jugadores, se cancela la partida :'(")
        for uid in game.get_users_list():
            user = users.get_user(uid)
            user.groupid = None
        games.del_game(game.group_id)

def start_voting(game):
    msgtext = "Hora de votar!\n\nEstas son las frases que habeis formado:"
    b = game.black_card
    picked_list = game.picked_cards
    keyboard = types.InlineKeyboardMarkup()
    for i in range(0, len(picked_list)):
        keyboard.add(types.InlineKeyboardButton(w_cards[picked_list[i][1]], callback_data=str(i)))
        msgtext += "\n\n{}. {}".format(i+1, b_cards[b].format(w_cards[picked_list[i][1]]))
    bot.send_message(game.group_id, msgtext)
    for c in picked_list:
        if self_voting:
            bot.send_message(c[0], "Hora de votar!\n\nElige la frase más divertida.\n\n{}".format(b_cards[game.black_card].format('_____')), reply_markup=keyboard)
        # else:
        #     #TODO - MODIFICAR TECLADO PARA NO MOSTRAR SU PROPIA CARTA
    game.voting = True

def show_result(game):
    winners = game.set_points()
    b = game.black_card
    if len(winners) == 1:
        msgtext = "Y el ganador de esta ronda es {}!!\n\n{}".format(game.users[str(winners[0][0])]['name'], b_cards[b].format(w_cards[winners[0][1]]))
    else:
        msgtext = "Los ganadores de esta ronda son:"
        for w in winners:
            msgtext += "\n\n{} - {}".format(game.users[str(w[0])]['name'], b_cards[b].format(w_cards[w[1]]))
    
    bot.send_message(game.group_id, msgtext)
    msgtext = "Recuento de puntos:"
    for u in game.users.values():
        msgtext += "\n{} - {} puntos".format(u['name'], u['points'])
    bot.send_message(game.group_id, msgtext)