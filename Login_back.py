from fastapi import FastAPI
from test_file import Register

app = FastAPI()

class system:
    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)

    def checklogin(self, username, passw):
        for u in self.user_list:
            if username == u.firstname:
                if passw == u.password:
                    return "Successfully"
        return "Not found"

s = system()
user1 = Register("Mr", "Racha",  "Tanagtaghoul", "racha@gmail.com","0816638801", "paul11")
s.add_user(user1)

@app.get("/")
async def root() -> dict:
    return {"Ping": "Pong"}

@app.post("/login_check")
async def call_logincheck(data : dict):
    usename_p = data["name_p"]
    password_p = data["pass_p"]
    status = s.checklogin(usename_p,password_p)
    return {"data" : status}
