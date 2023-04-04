#!/usr/bin/python3.11
"""
    @author Jack L.
    @name Entry.py
    @datelastmodified 2023 04 04
    @purpose Class handles user information.
"""
import getpass
import datetime
class User:
    default_user = { "name": getpass.getuser(), 
                     "role": "Operations Manager",
                     "company": "Eagle & Associates" }
    default_username = getpass.getuser()
    def __init__(self):
        self.today = datetime.datetime.now().strftime("%m %y %d — %H:%M:%S")
        self.username = self.default_user['name']
        self.role = self.default_user['role']
        self.companyname = self.default_user['company']
        self.user = { "name": self.username,
                       "role": self.role,
                       "company": self.companyname }
    def get_company(self):
        return self.companyname
    def get_current(self):
        return self.username
    def get_role(self):
        return self.role
    def set_company(self, new_company:str):
        try:
            self.companyname = self.new_company
        except ValueError:
            print("A string is needed here.")
    def set_current(self, new_username:str):
        try:
            self.username = new_username
        except ValueError:
            print("A string is needed here.")
    def set_role(self, new_role:str):
        try:
            self.role = new_role
        except ValueError:
            print("A string is needed here.")
    def greet( self ):
        print( self.today )
        print(f"Current User: { self.username }, { self.role } @ { self.companyname }.")
        print(f"Hello, { self.username }. Welcome to your WorkLog.\n")
    def view( self ):
        for key, value in self.user.items():
            print(key, value)
