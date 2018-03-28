from random import shuffle
from config import max_deals, cards_per_person, win_round_points, tie_round_points, rounds

class Game:
    def __init__(self, group_id, w_cards, b_cards):
        self.w_cards = range(0, w_cards)
        self.b_cards = range(0, b_cards)
        shuffle(self.w_cards)
        shuffle(self.b_cards)
        self.group_id = group_id
        self.users = {}
        self.started = False
        self.round = 0
    
    def new_round(self):
        if self.round == rounds:
            return False
        self.round += 1
        self.black_card = self.b_cards.pop()
        self.picked_cards = []
        self.voting = False
        for u in self.users.values():
            u['voted'] = False
        return True

    def get_users_list(self):
        return self.users.keys()
    
    def exist_user(self, user_id):
        return str(user_id) in self.users

    def join_user(self, user_id, user_name):
        if str(user_id) in self.users:
            return False
        else:
            self.users[str(user_id)] = { 'name':user_name, 'deals':max_deals+1, 'points':0, 'voted':False }
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
        if card in self.users[str(user_id)]['cards'] and not any(c[0] == user_id for c in self.picked_cards):
            index = self.users[str(user_id)]['cards'].index(card)
            self.users[str(user_id)]['cards'].pop(index)
            self.users[str(user_id)]['cards'].append(self.w_cards.pop())
            self.picked_cards.append([user_id, card, 0])
            return True
        else:
            return False

    def all_picked(self):
        return len(self.users) == len(self.picked_cards)
    
    def vote(self, user_id, num):
        if not self.users[str(user_id)]['voted'] and num < len(self.picked_cards):
            self.picked_cards[num][2] += 1
            self.users[str(user_id)]['voted'] = True
            return True
        else:
            return False
    
    def all_voted(self):
        return not any(u['voted'] == False for u in self.users.values())

    def set_points(self):
        self.picked_cards.sort(key=lambda x: x[2], reverse = True)
        winners = self.picked_cards
        max_points = winners[0][2]
        for i in range(1, len(winners)):
            if winners[i][2] != max_points:
                winners = winners[:i]
                break
        
        if len(winners) == 1:
            self.users[str(winners[0][0])]['points'] += win_round_points
        else:
            for w in winners:
                self.users[str(w[0])]['points'] += tie_round_points
        
        return winners

    def start(self):
        if len(self.users) < 3:
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
