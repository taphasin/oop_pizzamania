from test_file import Login

class System:
    def __init__(self):
        self.__user_list = []

    def add_user(self, e, p):
        self.__user_list.append(Login(e,p))

    def checklogin(self, username, passw):
        for u in self.__user_list:
            if username == u.email:
                if passw == u.password:
                    return "Successfully"
        return "Not found"

s = System()
s.add_user("Ta", "12345")
print(s.checklogin("Ta", "12345")) # should print "Successfully"
