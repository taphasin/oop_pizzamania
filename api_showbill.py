from fastapi import FastAPI

app = FastAPI()

class Payment:
    def __init__(self, payment_date, payment_status, order_id, total):
        self.payment_date = payment_date
        self.payment_status = payment_status
        self.order_id = order_id
        self.total = total

class Address:
    def __init__(self, mooban, house, roadname, soi, subsoi, district, provoince, postalcode):
        self.mooban = mooban
        self.house = house
        self.roadname = roadname
        self.soi = soi
        self.subsoi = subsoi
        self.district = district
        self.provoince = provoince
        self.postalcode = postalcode



class Bill:
    def __init__(self):
        self.address = None
        self.payment = None

    def add_address(self, address):
        self.address = address
    def add_payment(self, payment):
        self.payment = payment

    def showinfo(self):
        mylist = []
        mylist.append(self.address.mooban)
        mylist.append(self.address.house)
        mylist.append(self.payment.total)
        return mylist



payment1 = Payment("4sep","a", "a", 799 )
address1 = Address("17/4","buahapakdee", "Bamroongrat", "", "", "", "","10400")

bill1 = Bill()
bill1.add_address(address1)
bill1.add_payment(payment1)






@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ping": "Pong"}

# GET -- > Read Todo


@app.post("/getbill", tags=["bill"])
async def get_bill():  
    
    return {"showbill" : bill1.showinfo()}