class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class system:
    def __init__(self):
        self.user_list = []

    def add_user(self, e, p):
        self.user_list.append(Login(e,p))

    def checklogin(self, username, passw):
        for u in self.user_list:
            if username == u.email:
                if passw == u.password:
                    return "Successfully"
        return "Not found"

s = system()
s.add_user("Ta", "12345")
print(s.checklogin("Ta", "12345")) # should print "Successfully"
