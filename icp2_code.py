# -*- coding: utf-8 -*-
"""ICP2_700759361.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YVmT8K7JjqnTSxXuruqLCtMQq6mn7fXz

Write a program that takes two strings from the user: first_name, last_name. Pass these variables to fullname function that should return the (full name). For example: ▪ First_name = “your first name”, last_name = “your last name” ▪ Full_name = “your full name” Write function named “string_alternative” that returns every other char in the full_name string. Str = “Good evening” Output: Go vnn
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name

alternate_chars = full_name[::2]

print("Full Name:", full_name)
print("Alternate Characters:", alternate_chars)

"""Write a python program to find the wordcount in a file (input.txt) for each line and then print the output. o Finally store the output in output.txt file. Example: Input: a file includes two lines: Python Course Deep Learning Course Output: Python Course Deep Learning Course Word_Count: Python: 1 Course: 2 Deep: 1 Learning: 1"""

text = open("input.txt", "r")
d = dict()
for line in text:
  line = line.strip()
  line = line.lower()
  words = line.split(" ")
  for word in words:

        if word in d:

            d[word] = d[word] + 1
        else:

            d[word] = 1


for key in list(d.keys()):
    print(key, ":", d[key])

"""Write a program, which reads heights (inches.) of customers into a list and convert these heights to centimeters in a separate list using: 1) Nested Interactive loop. 2) List comprehensions"""

lst1 = []
n = int(input("enter number of customers: "))
for i in range(n) :
  height = int(input ("Enter the height of customers in inches: "))
  lst1.append(height)
lst1 = [height * 2.54 for height in lst1]
print(lst1)