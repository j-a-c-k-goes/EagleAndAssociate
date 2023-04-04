#!/usr/bin/python3.11
"""
    @name app.py
    @datelastmodified 2023 04 04
    @purpose Runs classes as main application.
"""
import LogAPI.User as User
import LogAPI.Entry as Entry
import LogAPI.LogHandler as LogHandler

if __name__ == "__main__":
	# Demo
	user = User.User()
	entry = Entry.Entry()
	log_handler = LogHandler.LogHandler()
	user.greet()
	log_handler.read_recent()
	entry.input()
	entry.view_all()
	entry.output()
	log_handler.get_log_list()
