class Game:
    users = {}

    def __init__(self, group_id):
        self.group_id = group_id
    
    def get_users_list(self):
        return self.users
    
    def exist_user(self, user_id):
        return str(user_id) in self.users

    def join_user(self, user_id, user_name):
        if str(user_id) in self.users:
            return False
        else:
            self.users[str(user_id)] = [user_name]
            return True

class Games_list:
    games_list = {}
    
    def new_game(self, group_id):
        if str(group_id) in self.games_list:
            return False
        self.games_list[str(group_id)] = Game(group_id)
        return True

    def get_game(self, group_id):
        if str(group_id) in self.games_list:
            return self.games_list[str(group_id)]
        else:
            return False