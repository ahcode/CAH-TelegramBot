# -*- coding: utf-8 -*-

import telebot
from CAH import *
from utils import new_round

@bot.message_handler(func=lambda message: message.chat.type == 'private', commands=['start'])
def start(m):
    users.register_user(m.from_user.id)
    bot.reply_to(m, "Gracias por hablarme! me sentia muy solo :( ahora puedes jugar partidas!")

@bot.message_handler(commands=['help'])
def help(m):
    bot.reply_to(m, "A ti te voy a ayudar yo...")

@bot.message_handler(func=lambda message: message.chat.type == 'group' or message.chat.type == 'supergroup' , commands=['new_game'])
def new_game(m):
    if games.new_game(m.chat.id, n_w_cards, n_b_cards):
        bot.send_message(m.chat.id, "Vamos a jugar!\n/join para unirte a la partida")
        join(m)
    else:
        bot.reply_to(m, "Tranquilito, que ya se está jugando una partida, no doy para tanto")

@bot.message_handler(func=lambda message: message.chat.type == 'group' or message.chat.type == 'supergroup' , commands=['join'])
def join(m):
    g = games.get_game(m.chat.id)
    if g == None:
        bot.reply_to(m, "Pero si no estamos jugando...\nUtiliza /new_game para empezar una partida")
    elif g.exist_user(m.from_user.id):
        bot.reply_to(m, "Desgraciado, que ya te has unido, no me lies")
    elif g.started:
        bot.reply_to(m, "La partida ya ha empezado, espabila para la próxima")
    else:
        try:
            bot.send_message(m.from_user.id, 'Te has unido a la partida en el grupo "{}"'.format(m.chat.title))
            g.join_user(m.from_user.id, m.from_user.first_name.encode("utf-8"))
            bot.send_message(m.chat.id, "{} se ha unido a la partida".format(m.from_user.first_name.encode("utf-8")))
        except telebot.apihelper.ApiException as e:
            if e.result.status_code == 403:
                bot.reply_to(m, "¿Ni te presentas? Mándame por privado /start para que te conozca un poco")

@bot.message_handler(func=lambda message: message.chat.type == 'group' or message.chat.type == 'supergroup' , commands=['force_start'])
def force_start(m):
    g = games.get_game(m.chat.id)
    if g == None:
        bot.reply_to(m, "Pero si no estamos jugando...\nUtiliza /new_game para empezar una partida")
    elif g.started:
        bot.reply_to(m, "Que vas a forzar si ya ha empezado listillo")
    else:
        g.start()
        bot.send_message(m.chat.id, "Por fin! La partida acaba de empezar!")
        new_round(g)

@bot.callback_query_handler(func=lambda call: hasattr(call, 'data') and call.message.chat.type == 'private')
def pick_card(call):
    print ("Hola")
    u = users.get_user(call.from_user.id)
    if u != None:
        g = games.get_game(u.groupid)
        if g != None:
            if call.data == 'deal':
                new_cards = g.deal(u.id)
                if new_cards == False:
                    bot.send_message(call.from_user.id, "No te pases, ya has barajado bastante")
                #else:
                    #imprimir cartas
            else:
                try:
                    c = int(call.data)
                    card = g.pick_card(c)
                    if card:
                        bot.send_message(call.from_user.id, "Has elegido \"{}\"".format(w_cards[card]))
                except ValueError:
                    pass
