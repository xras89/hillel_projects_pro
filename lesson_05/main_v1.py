"""
Download rockyou file
Create an application that allows you to input the string
Then, the application goes through the whole file 
and checks if the requested string exists in each line
Then, it shows to user how many lines have been found during the search process
additional

The file is quite huge so it should be added to the .gitignore"""

import time


def high_precision():
    start_time = time.time()
    with open("rockyou.txt", "r", encoding="latin-1") as file:
        count = 0

        for line in file:
            fix_line = line.replace("\n", "")
            if search_string == fix_line:
                count += 1

    stop_time = time.time()
    print(f"Lines found: {count}")
    print(f"Operating time: {stop_time - start_time} sec")


def low_precision():
    start_time = time.time()

    with open("rockyou.txt", "r", encoding="latin-1") as file:
        list_of_lists = [
            word.replace("\n", "").lower() for word in file.readlines()
        ]
        count = 0

        for item in list_of_lists:
            if search_string in item:
                count += 1

    stop_time = time.time()

    print(f"Lines found: {count}")
    print(f"Operating time: {stop_time - start_time} sec")


search_precision = int(
    input("Select precision for search ('1' is high, '2' is low)\n")
)
search_string = input("Enter the search string: ")

if search_precision == 1:
    high_precision()
elif search_precision == 2:
    low_precision()
else:
    print("Wrong precision select, only '1' or '2'1 can be entered")
