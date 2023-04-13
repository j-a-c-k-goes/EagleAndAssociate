#!/usr/bin/python3.11
"""
    @author Jack L.
    @name Entry.py
    @datelastmodified 2023 04 13
    @purpose Class handles work log entries.
"""

# import modules
import datetime
import os.path

class Entry:
    def __init__(self):
        self.current = None         # Current Entry
        self.entries = dict()       # This session's entries. { 'date': 'entry' }
        self.date = datetime.datetime.now().strftime(f"%y-%m-%d_%H%M%S")
        self.destination = "./LogFiles/"
    def get_current(self):
        return self.current
    def get_entries(self):
        return self.entries
    def set_current(self, current_entry:str):
        try:
            self.current = current_entry
        except TypeError:
            print("A String is required.")
    def set_destination(self, new_destination:str):
        try:
            self.destination = new_destination
        except TypeError:
            print("A string is required.")
    def input(self):
        try:
            counter = 0
            making_an_entry = True
            print("\n---- Making an Entry ---")
            while making_an_entry:
                entry = str( input("Type your ❤️ in >>> ") )
                self.set_current(entry)
                date = datetime.datetime.now().strftime(f"%y-%m-%d_{counter}")
                # time = datetime.datetime.now().strftime("%H:%M")
                self.entries[ date ] = entry
                self.get_current()
                confirm = str(input("Still making entries??? (y / n) "))
                if confirm.lower() == "y":
                    counter += 1
                else:
                    making_an_entry = False
                    break
                print("Entries made:", counter)
        except TypeError:
            print("the entry should be a string.")
    def edit(self, entry_to_edit:str):
        try:
            fallbackValue = "[ entry does not exist ]"
            edit_this_entry = self.entries.get(entry_to_edit, fallbackValue)
            editing_an_entry = True
            while editing_an_entry:
                if edit_this_entry.lower() == fallbackValue:
                    print("There is no entry with this key ( date ). Exiting function.")
                    break
                if ( edit_this_entry is not False or edit_this_entry is not None) and (edit_this_entry is not fallbackValue):
                    print(f"---- Entry being edited: { edit_this_entry } ----")
                    new_content = str( input( "Enter the new content >>> " ) )
                    print("Your new content:", new_content)
                    confirm = str( input( "Is this ok? y / n >>> " ) )
                    if confirm.lower() == "y":
                        self.entries[entry_to_edit] = new_content
                        editing_an_entry = False
                        break
                    else:
                        print( "Ok, enter the correct content. This will replace the entry selected." )
                else:
                    print( "There are no entries with this key:", entry_to_edit )
        except TypeError:
            print( "An exception has occured." )
            print( "Most likely cause: Missing key." )
            print( "Also possible: You did not pass in a string." )
    def output( self ):
        try:
            there_are_entries = (len( self.entries ) != 0)
            if there_are_entries:
                filename = f"log_{ self.date }.txt"
                final_destination = f"{ self.destination }{ filename }"
                print("Setting absolute path @", final_destination)
                with open(final_destination, "a") as file:
                    for key, value in self.entries.items():
                        file.write( f"{ key }\t{ value }\n" )
                print("Done writing to", filename)
            else:
                print("There are no entries to write.")
                return False
        except FileNotFoundError:
            print( "Invalid destination", self.destination )
        except TypeError:
            print( "Method requires a string." )
    def view_current(self):
        current = self.get_current()
        print(current) 
    def view_all( self ):
        for key, value in self.entries.items():
            print( f"{ key }\t{ value }" )
        print( "Done." )
