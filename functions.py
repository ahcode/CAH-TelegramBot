# -*- coding: utf-8 -*-

import telebot
from CCH import bot, users, games

@bot.message_handler(func=lambda message: message.chat.type == 'private', commands=['start'])
def start(m):
    users.register_user(m.from_user.id, m.chat.id)
    bot.reply_to(m, "Gracias por hablarme! me sentia muy solo :( ahora puedes jugar partidas!")

@bot.message_handler(commands=['help'])
def help(m):
    bot.reply_to(m, "A ti te voy a ayudar yo...")

@bot.message_handler(func=lambda message: message.chat.type == 'group' or message.chat.type == 'supergroup' , commands=['new_game'])
def new_game(m):
    if games.new_game(m.chat.id):
        try:
            bot.send_message(m.from_user.id, 'Te has unido a la partida en el grupo "' + m.chat.title + '"')
        except telebot.apihelper.ApiException as e:
            if e.result.status_code == 403:
                bot.reply_to(m, "¿Ni te presentas? Mándame por privado /start para que te conozca un poco")
    else:
        bot.reply_to(m, "Tranquilito, que ya se está jugando una partida, no doy para tanto")