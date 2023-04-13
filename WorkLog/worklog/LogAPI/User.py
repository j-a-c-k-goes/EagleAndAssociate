#!/usr/bin/python3.11
"""
    @author Jack L.
    @name Entry.py
    @datelastmodified 2023 04 13
    @purpose Class handles user information.
"""
import getpass
import datetime
import pyinputplus as validateinput
class User:
    default_user = { "name": getpass.getuser(), 
                     "role": "Technology & Design Lead",
                     "company": "NeoITD" }
    default_username = getpass.getuser()
    def __init__(self):
        self.today = datetime.datetime.now().strftime("%m %y %d — %H:%M:%S")
        self.username = self.default_user[ "name" ]
        self.role = self.default_user[ "role" ]
        self.companyname = self.default_user[ "company" ]
        self.user = { "name": self.username,
                      "role": self.role,
                      "company": self.companyname }
    def get_company(self):
        return self.companyname
    def get_role(self):
        return self.role
    def get_username(self):
        return self.username
    def get_user(self):
        return self.user
    def set_company(self, new_company:str):
        try:
            self.companyname = new_company
        except ValueError:
            print("A string is needed here.")
    def set_role(self, new_role:str):
        try:
            self.role = new_role
        except ValueError:
            print("A string is needed here.")
    def set_user(self):
        self.user["name"] = self.get_username()
        self.user["role"] = self.get_role()
        self.user["company"] = self.get_company()
    def set_username(self, new_username:str):
        try:
            self.username = new_username
        except ValueError:
            print("A string is needed here.")
    def greet( self ):
        print(f"\n---- { self.username.upper() } ----")
        print(f"{ self.username } is the { self.role } @ { self.companyname }")
        print( "Date:", self.today )
    def edit(self):
        print("Editing the current user:\n")
        what_can_be_edited = [ "username", "role", "companyname", "everything" ]
        i_am_editing_this = validateinput.inputMenu( choices=what_can_be_edited, numbered=False)
        def new_username():
            prompt = "Enter a new username >>> "
            new_username = validateinput.inputStr( prompt=prompt, timeout=120)
            self.set_username( new_username )
        def new_role():
            prompt = "Enter a new role >>> "
            new_role = validateinput.inputStr( prompt=prompt, timeout=120, limit=5)
            self.set_role( new_role )
        def new_company():
            prompt = "Enter a new organization >>> "
            new_company = validateinput.inputStr( prompt=prompt, timeout=120, limit=5)
            self.set_company( new_company )  
        match i_am_editing_this:
            case "username":
                new_username()
            case "role":
                new_role()
            case "companyname":
                new_company()
            case "everything":
                 new_username()
                 new_role()
                 new_company()
            case _:
                print("Not a possible item to edit.")
                return False
        self.set_user()
    def view( self ):
        print("User details:\n")
        for key, value in self.user.items():
            print(f"{key.upper()}\t\t{value.upper()}")
