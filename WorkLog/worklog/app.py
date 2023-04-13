#!/usr/bin/python3.11
"""
    @name app.py
    @datelastmodified 2023 04 04
    @purpose Runs classes as main application.
"""
import os
import sys
import time
import LogAPI.Entry as Entry
import LogAPI.LogHandler as LogHandler
import LogAPI.Menu as Menu
import LogAPI.User as User
def title():
	print("---------------------")
	print("WWWW    WWWW    WWWW")
	print("OOOO    OOOO    OOOO")
	print("RRRR    RRRR    RRRR")
	print("KKKK    KKKK    KKKK")
	print("---------------------")
def demo_context():
	""" 
	    Main loop runs as a demonstration.
	    Note: Treat this as a base model until\
	    further interaction is implemented.
	"""
	print("WorkLog 1.0.0\tRunning in demo mode as base model.")
if __name__ == "__main__":
	demo_context()
	title()
	# Instantiate Neccessary Classes
	log_handler = LogHandler.LogHandler()
	entry = Entry.Entry()
	user = User.User()
	mainmenu = Menu.MainMenu()
	helpmenu = Menu.HelpMenu()
	
	# Handle app.py without arguments.
	noArgumentsMade = len(sys.argv) < 2
	if noArgumentsMade:
		print( "Mode: Using application in freestyle mode.\n" )
		helpmenu.view()
	
	# Handle arguments
	else:
		your_argument = sys.argv[1]
		match your_argument:
			case "make_entry":
				pass
			case "last_batch":
				pass
			case "entry_history":
				pass
			case "view_user":
				user.view()
			case "edit_user":
				user.edit()
			case "get_help":
				helpmenu.view()
			case _:
				print(your_argument, "is not valid.")
				helpmenu.view()
	# Demo Flow
	# log_handler.get_log_list()
	# log_handler.read_recent()
	# demo_is_live = True
	# demo_runs = 0
	# while demo_is_live:
	# 	demo_runs += 1
	# 	user.greet()
	# 	menu.view()
	# 	menu.select_option()
	# 	entry.input()
	# 	entry.output()
	# 	time.sleep(1)
	# 	entry.view_all()
	# 	time.sleep(3)
	# 	os.system("clear")
	# 	if demo_runs > 3:
	# 		print("DEMO OVER 😊")
	# 		time.sleep(2)
	# 		demo_is_live = False
	# 		break
