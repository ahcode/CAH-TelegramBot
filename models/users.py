import json
from config import json_users_file

class User:
    def __init__(self, uid, points):
        self.id = uid
        self.groupid = None
        self.points = points
    
    def set_game(self, groupid):
        self.groupid = groupid

class Users:
    def __init__(self):
        self.users_list = {}
    #     try:
    #         fich = open(json_users_file, "r")
    #         users_dic = json.loads(fich.read())
    #         fich.close()
    #         for key, value in users_dic.iteritems():
    #             self.users_list = User(int(key), value)
    #     except IOError:
    #         pass

    # def __save(self):
    #     fw = open(json_users_file, "w")
    #     fw.write(json.dumps(self.users_list))
    #     fw.close()

    def register_user(self, user_id):
        if str(user_id) not in self.users_list:
            self.users_list[str(user_id)] = User(user_id, 0)
            #self.__save()

    def get_user(self, user_id):
        if str(user_id) in self.users_list:
            return self.users_list[str(user_id)]
        else:
            return None