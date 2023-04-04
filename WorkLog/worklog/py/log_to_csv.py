# - - - import csv module - - -
import csv
row_1 = ["date", "entry"]

with open("data/personal_log.csv", "w") as csv_file:
	# - - - use writer class to create writer object - - -
	writer = csv.writer(csv_file, delimiter=",")
	writer.writerow(row_1)