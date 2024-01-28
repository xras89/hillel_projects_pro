"""
Download rockyou file
Create an application that allows you to input the string
Then, the application goes through the whole file 
and checks if the requested string exists in each line
Then, it shows to user how many lines have been found during the search process
additional

The file is quite huge so it should be added to the .gitignore"""

import time

search_string = input("Enter the search string: ")

count = 0

start_time = time.time()

with open("rockyou.txt", "r", encoding="latin-1") as file:
    list_of_lists = [
        word.replace("\n", "").split() for word in file.readlines()
    ]

    for item in list_of_lists:
        if search_string in item:
            print(item)
            count += 1

stop_time = time.time()

print(f"Lines found: {count}")
print(f"Operating time: {stop_time - start_time} sec")
