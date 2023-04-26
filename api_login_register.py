from fastapi import FastAPI
from test_file import Register

app = FastAPI()

class system:
    def __init__(self):
        self.user_list = []

    def add_new_user_in_user_list(self, user):
        self.user_list.append(user)
        return "sucessful"

    def checklogin(self, username, passw):
        for u in self.user_list:
            if username == u.firstname:
                if passw == u.password:
                    return "Successfully"
        return "Not found"

s = system()
#user1 = Register("Mr", "Racha",  "Tanagtaghoul", "racha@gmail.com","0816638801", "paul11")
#s.add_user(user1)

@app.post("/login_check")
async def call_logincheck(data : dict):
    usename_p = data["name_p"]
    password_p = data["pass_p"]
    status = s.checklogin(usename_p,password_p)
    return {"data" : status}

@app.post("/Register")
async def call_logincheck(data : dict):
    prefix_c = data["prefix_p"]
    fname_c  = data["fname_p"]   
    lname_c  = data["lname_p"]
    email_c  = data["email_p"]
    mobile_c = data["mobile_p"]
    pass_c   = data["pass_p"]
    person = Register(prefix_c,fname_c,lname_c,email_c,mobile_c,pass_c)
    status = s.add_new_user_in_user_list(person)
    return {"data" : status}