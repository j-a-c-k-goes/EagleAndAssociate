#!/usr/bin/python3.11
"""
    @name app.py
    @datelastmodified 2023 04 04
    @purpose Runs classes as main application.
"""
import LogAPI.User as User
import LogAPI.Entry as Entry
import LogAPI.LogHandler as LogHandler
import os
import time
if __name__ == "__main__":
	""" Main loop runs as a demonstration.

	    Note: Treat this as a base model until\
	    further interaction is implemented.

	"""
	# Instantiate Classes
	log_handler = LogHandler.LogHandler()
	entry = Entry.Entry()
	user = User.User()

	# Demo Flow
	log_handler.get_log_list()
	log_handler.read_recent()
	demo_is_live = True
	demo_runs = 0
	while demo_is_live:
		demo_runs += 1
		user.greet()
		entry.input()
		entry.output()
		time.sleep(1)
		entry.view_all()
		time.sleep(3)
		os.system("clear")
		if demo_runs > 3:
			print("DEMO OVER 😊")
			time.sleep(2)
			demo_is_live = False
			break
