#!/usr/bin/python3.11
"""
    @author Jack L.
    @name LogHandler.py
    @datelastmodified 2023 04 04
    @purpose Class handles work log entries.
"""
import os
class LogHandler:
    def __init__(self):
        self.log_directory = "./LogFiles/"
        self.deleted_logs = dict()
    def get_log_list(self):
        try:
            print("These are current log files:\n")
            for file in os.listdir(self.log_directory):
                if file[0] == ".":
                    print("Hidden file.")
                else:
                    print( file )
        except FileNotFoundError:
            print("An invalid path has been provided.")
    def delete_log(self, log_name:str):
        try:
            print("Preparing to delete", log_name)
            log_to_delete = f"{ self.log_directory }{ log_name }"
            with open(log_to_delete, "r+") as source:
                self.deleted_logs['log_name'] = source.read()
            os.remove(log_to_delete)
            print(f"Done. { log_name } has been deleted.")
        except TypeError:
            print("Use a string to delete the log.")
        except FileNotFoundError:
            print("Invalid path.")
    def read_entry(self, log_name:str):
        try:
            print("Reading", log_name)
            path = f"{ self.log_directory }{ log_name}"
            with open(path, "r") as source:
                print(source.read())
        except TypeError:
            print("Use a string as the pass-in value.")
        except FileNotFoundError:
            print(log_name, "Does not exist.")
    def read_recent(self):
        try:
            print("This is the most recent log's entries:")
            if (len(os.listdir(self.log_directory))) > 0:
                most_recent = (os.listdir(self.log_directory)[-1])
                path = f"{ self.log_directory }{ most_recent }"
                with open(path, "r") as source:
                    print(source.read())
                print("Done.")
            else:
                print("There are no logs to read.")
        except FileNotFoundError:
            print("Invalid path.")
    def view_deleted(self):
        print("These are the recently deleted journal entries.")
        print(self.deleted_logs)
