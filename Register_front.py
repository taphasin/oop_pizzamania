from fastapi import FastAPI
from test_file import Register

app = FastAPI()

class System:
    def __init__(self):
        self.user_list = []
    
    def add_user_in_user_list(self, user):
        self.user_list.append(user)
        return "sucessful"

u = System()

@app.get("/listuser")
async def h():
    return {"data" : u.user_list}

@app.post("/Register")
async def call_logincheck(data : dict):
    prefix_c = data["prefix_p"]
    fname_c  = data["fname_p"]   
    lname_c  = data["lname_p"]
    email_c  = data["email_p"]
    mobile_c = data["mobile_p"]
    pass_c   = data["pass_p"]
        
    person = Register(prefix_c,fname_c,lname_c,email_c,mobile_c,pass_c)
    status = u.add_user_in_user_list(person)

    return {"data" : status}
