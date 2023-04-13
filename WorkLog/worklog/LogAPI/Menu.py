#!/usr/bin/python3.11
"""
    @author jack l.
    @name Entry.py
    @datelastmodified 2023 04 13
    @purpose Class handles Menu build.
"""
import pyinputplus as validateinput
class MainMenu:
    def Print(self):
        print("MainMenu called.")
    default_menu = { 
                     "make_entry":      { "command":"make_entry", 
                                          "desc": "make a new entry" },
                     "edit_entry":      { "command":"edit_entry", 
                                          "desc": "edit an entry (this session)" },
                     "save_session":    { "command": "save_session", 
                                          "desc": "save entries (this session)"},
                     "current_entry":   { "command": "current_entry",
                                          "desc": "current_entry"}, 
                     "session_entries": { "command": "session_entries", 
                                          "desc": "view session's entries"},
                     "last_batch":      { "command": "last_batch", 
                                          "desc": "last saved batch of entries"},
                     "entry_history":   { "command": "entry_history", 
                                          "desc": "view file log"},
                     "delete_file":     { "command": "delete_file", 
                                          "desc": "delete a specific file" },
                     "view_user":       { "command": "view_user", 
                                          "desc": "view user details"},
                     "edit_user":       { "command": "edit_user", 
                                          "desc": "edit current user"},
                     "quit_session":    { "command": "quit_session", 
                                          "desc": "quit session" },
                     "get_help":        { "command": "get_help", 
                                          "desc": "displays the help menu"}
                }
    def __init__( self ):
        self.options = self.default_menu
        self.option = None
    def choose_option(self):
        selecting_option = True
        while selecting_option:
            try:
                menuOptions = [ key for key in self.options.keys() ]
                choice = validateinput.inputMenu(menuOptions)
                #option = str( input( ">>> " ) )
                #confirm_option = validateinput.inputYesNo("Proceed with this? [ y / n ] >>> ")
                #if confirm_option.lower() == "y":
                print( "Selected option:", choice )
                self.set_option(choice)
                return choice
                selecting_option = False
            except Exception:
                print("...")
    def get_options( self ):
        return self.options
    def set_option( self, option_to_set ):
        self.option = self.options[ option_to_set ]
    def view(self):
        print( f"\nMenu Options:\n" )
        for key, value in self.options.items():
            print( f"{ key }\t\t{ value } ")
        print( "------------------------------------------------" )
class HelpMenu(MainMenu):
    def Print(self):
        print("HelpMenu called.")
    def __init__(self):
        MainMenu.__init__(self)
    def view(self):
        print( "Usage: python app.py [ argument ] ( FLAGS ARE NOT REQUIRED )\n")
        print("Available Commands:\n")
        for key, value in self.options.items():
            print( f"{ value[ 'command' ] }\t\t\t{ value[ 'desc' ] }" )
        print( "------------------------------------------------" )