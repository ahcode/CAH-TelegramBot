import telebot
from TOKEN import TOKEN
from models.users import Users
from models.games import Games_list

users = Users()
games = Games_list()
bot = telebot.TeleBot(TOKEN, skip_pending=True)