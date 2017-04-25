#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: phonebook.py
# Author: SHUANG LUO

import os
path = os.path.expanduser(r"~/Desktop/myphonebook.txt")
phonebook_content = open(path).read()
c = phonebook_content.split('\n')
print (c) # this line is used to print out the context of myphonebook.text which can be removed
flag = 0 # means the user's name is not found
print ("This is a phonebook")
print ("Type into user name for searcing his/her TEL_NUMBER, in the form of (Last_name first_name)")
print ("'QUIT' for quit this phonebook")
user_input = input("Please, type a name: ")
if user_input == "QUIT" :
    print ("Thank you for using this excellent phone number application!")
    print ("Good Bye!")
    flag = 2 # means the user want to quit
for element in c:
    each_info = element.split(":")
    if each_info[0] == user_input:
        print(each_info[1])
        flag = 1 # means the user's name is found
        break
if flag == 0 :
    print("Phone number is not available")

