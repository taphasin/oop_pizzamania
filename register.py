class Person:
    def __init__(self, firstname, lastname, address, log_in,  account_status):
        self._firstname = firstname
        self._lastname = lastname
        self._addressid = [address]
        self._loginid = log_in
        self._account_status = account_status