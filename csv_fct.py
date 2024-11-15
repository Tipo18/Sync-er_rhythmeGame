import os
import csv

print("launch")

file_name = "tim.csv"



def csv_init(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([""])
            print(f"{file_name} created.")
    else:
        print(f"{file_name} already exists.")


def csv_end():
    print("")

csv_init(file_name)