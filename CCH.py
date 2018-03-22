import telebot
from TOKEN import TOKEN
from users import Users
from games import Games

users = Users()
games = Games()
bot = telebot.TeleBot(TOKEN, skip_pending=True)