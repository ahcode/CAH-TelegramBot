import telebot
from TOKEN import TOKEN
from models.users import Users
from models.games import Games_list
from cards import load_cards

users = Users()
games = Games_list()
n_w_cards, n_b_cards, w_cards, b_cards = load_cards()

bot = telebot.TeleBot(TOKEN, skip_pending=True)