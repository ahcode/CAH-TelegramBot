from random import shuffle
from config import max_deals, cards_per_person

class Game:
    def __init__(self, group_id, w_cards, b_cards):
        self.w_cards = range(0, w_cards)
        self.b_cards = range(0, b_cards)
        shuffle(self.w_cards)
        shuffle(self.b_cards)
        self.group_id = group_id
        self.users = {}
        self.new_black_card()
        self.started = False
    
    def new_black_card(self):
        self.black_card = self.b_cards.pop()
        self.picked_cards = {}
        return self.black_card

    def get_users_list(self):
        return self.users.keys()
    
    def exist_user(self, user_id):
        return str(user_id) in self.users

    def join_user(self, user_id, user_name):
        if str(user_id) in self.users:
            return False
        else:
            self.users[str(user_id)] = { 'name':user_name, 'deals':max_deals+1 }
            self.deal(user_id)
            return True
    
    def deal(self, user_id):
        if str(user_id) in self.users:
            if self.users[str(user_id)]['deals'] > 0:
                self.users[str(user_id)]['deals'] -= 1
                self.users[str(user_id)]['cards'] = self.w_cards[:10]
                self.w_cards = self.w_cards[10:]
                return self.users[str(user_id)]['cards']
            else:
                return False
        else:
            return None

    def pick_card(self, user_id, card):
        if card in self.users[str(user_id)]['cards'] and str(user_id) not in self.picked_cards:
            index = self.users[str(user_id)]['cards'].index(card)
            self.users[str(user_id)]['cards'].pop(index)
            self.users[str(user_id)]['cards'].append(self.w_cards.pop())
            self.picked_cards[str(user_id)] = card
            return True
        else:
            return False

    def start(self):
        if len(self.users) <= 3:
            return False
        else:
            self.started = True
            return True
    
    def get_cards(self):
        cards = {}
        for uid in self.users.keys():
            cards[uid] = self.users[uid]['cards']
        return cards

class Games_list:
    games_list = {}
    
    def new_game(self, group_id, w_cards, b_cards):
        if str(group_id) in self.games_list:
            return False
        self.games_list[str(group_id)] = Game(group_id, w_cards, b_cards)
        return True

    def get_game(self, group_id):
        if str(group_id) in self.games_list:
            return self.games_list[str(group_id)]
        else:
            return None

    def del_game(self, group_id):
        if str(group_id) in self.games_list:
            del self.games_list[str(group_id)]
