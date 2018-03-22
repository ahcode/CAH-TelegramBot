class Games:
    games_list = {}
    
    def new_game(self, group_id):
        if str(group_id) in self.games_list:
            return False
        self.games_list[str(group_id)] = [] #Por Definir
        return True
