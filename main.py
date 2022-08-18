import datetime
import os
from pathlib import Path

currentDT = datetime.datetime.now()

# Ask user to input weight in lbs

value = input("Enter Weight in KG: ")

#value = 77.9

# store weight in to text file

file_exists = os.path.exists(
    '/Users/Jak.Bustin/Documents/weight_tracker/weight.txt')

if file_exists == True:
    print("File Exists!")
    create = open("weight.txt", "a")
    create.write("{:>20} {:>20}\n".format(str(currentDT), value))
    create.close()
else:
    print("File does not exist, creating file...")
    # create file with header
    create = open("weight.txt", "a")
    create.write("{:>20} {:>20}\n".format("Date", "Weight"))
    create.write("{:>20} {:>20}\n".format(str(currentDT), value))
    create.close()

# read each line, and strip /n

with open("weight.txt") as l:
    content = l.readlines()

li = [x.strip() for x in content]


count = 0
empty_list = []


for x in range(len(content)):
    empty_list.append(li[count][-4:])
    count = count + 1

# read from text file, and print to screen

f = open("weight.txt", "r")

print(f.read())

# assign last 7 elements from list

average_list = empty_list[-7:]

integer_list = [float(z) for z in average_list]

answer = sum(integer_list)

# print average of last 7 days

print("Average for last 7 days: ", answer / 7)
