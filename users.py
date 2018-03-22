import json
from config import json_users_file

class Users:
    def __init__(self):
        try:
            fich = open(json_users_file, "r")
            self.users_list = json.loads(fich.read())
            fich.close()
        except IOError:
            self.users_list = {}

    def __save(self):
        fw = open(json_users_file, "w")
        fw.write(json.dumps(self.users_list))
        fw.close()

    def register_user(self, user_id, private_chat_id):
        if str(user_id) not in self.users_list:
            self.users_list[str(user_id)] = 0
            self.__save()
