from test_file import Register
class System:
    def __init__(self):
        self.__user_list = []

    def add_user_in_user_list(self, user):
        self.__user_list.append(user)

    def prin(self):
        for i in self.user_list:
            print("name" + i.firstname) 

system = System()
user1 = Register("Mr", "Racha",  "Tanagtaghoul", "racha@gmail.com","0816638801", "paul11")
system.add_user_in_user_list(user1)

system.prin()

