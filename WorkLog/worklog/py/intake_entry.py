# import modules
from datetime import date
from edit_entry import *
import csv
import os.path

# bind empty list to variable 
thoughts = list()

# input a thought
def input_thought():
	print("ready for input")
	try:
		input_thought = str(input("enter your thought for today: "))
	except ValueError:
		print("ok, this is not valid syntax. please type a string/phrase/words.")
	print("input received")
	return input_thought

# collect thoughts
def collect_thought(thoughts):
    print("collecting thgouht for work log.")
    thoughts.append( { "date": date.today(), "thought":input_thought() })
    return thoughts

# prompt to contine entering thoughts
def prompt_to_continue():
    status = str(input("would you like to continue? type y or n for [yes/no]: "))
    status = status.lower()
    return status

# write content to file
def write_to_txt_file(file_name, data):
    file = open(file_name, "a")
    print(f"{file_name} opened")
    file.write(data)
    print(f"done writing to {file_name}")

# print entered thoughts
def print_thoughts(thoughts):
    print("entries:")
    for element in thoughts:
        print(f"{element['date']}\t{element['thought']}")
        print("end of entries")

# on run / export
if __name__ == "__main__":
    # define destination file
    destination_file = "../log/work_log.txt"
    
    # boolean for entries
    entering_thoughts = True
    
    # begin loop, entering data
    while entering_thoughts is True:
        collect_thought(thoughts)
        if prompt_to_continue() == "n":
            print("completed collecting thoughts")
            entering_thoughts = False
            if len(thoughts) == 0:
                print("no thoughts have been entered.")
            else:
                print_thoughts(thoughts)
        else:
            continue
    # loop exited, iterate through built result
    for thought in thoughts:
        write_to_txt_file(
        destination_file,
        f"""
{thought['date']}
{thought['thought']}
--------------------
"""
        )

