# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:48:40 2017
@author: Nichollette

This is a basic script for the fMRI workshop Python Basic Lesson
This is how you do a block comment
"""

# This is how you do individual comments


variableI = 100 # This is an Integer 
variableF= 100.30 # This is a Float 
variableB = True # This is a Boolean 
variableS = "fMRI Workshop 2017" # This is a String
print("Integer: %d\n" % (variableI) +  "Float:  %d\n" % (variableF) 
        + "Boolean:  %s\n" %(variableB) + "String: %s" %(variableS))  



# Lists in Python
def makeList():
    nationalParks = ['Yosemite', 'Grand Canyon', "Zion", "Bryce", "Arches"]
    squares = [1, 4, 9, 16]
    print("Index 0 of National Parks list: " + nationalParks[0])

def appendList(userInput):
    nationalParks.append(userInput)
    print(nationalParks)

def sortList():
    print(nationalParks)
    nationalParks.sort()
    print(nationalParks)


sum = 0
for num in squares:
    sum += num
print("Sum of Squares list: " + str(sum))

def makeDictionary():
    
    # empty dictionary
    my_dict = {}

     # dictionary
    my_dict= {
        'Name' : 'Leo',
        'Species': 'Cat', 
        'Age': 7
        }
    print(my_dict)
    print("dict['Name']:", my_dict['Name'], "\ndict['Species']:", my_dict['Species'], "\ndict['Age']):", my_dict['Age'])
    
  






def dictionaryExamples(selection):
    switch (selection): {
        case 0:
           # if "Name" in my_dict: 
                   # print("TRUE");
            break;
        case 1:
            my_dict['Age'] = 8; # update Dictionary
            print("Updated dict['Age']", my_dict['Age']);
            break;
        case 2:
            my_dict['BloodType'] = 'A';  # Add new entry
            print(dict);
            break;
        default:
            break;
            
        }
# compound statements

# if statement
# colon (:) is required, separates the HEADER from the BODY
# example:  
#       if BOOLEAN EXPRESSION:
#           STATEMENTS 

# The line after the colon must be indented - Python standard 4 spaces
# (==)


    
def ifExamples():
    
    
    if variableB is True: #  10 > 5, 5 > 10
        print("Condition is TRUE. I am in the if block.")
    else:
        print("Condition is FALSE. I am in else block.")


    if 'Yosemite' in nationalParks:
        print("Found 'Yosemite' in our list")
    

# The for loop processes each item in a sequence, so it is used with Python’s sequence data types - strings, lists, and tuples.
# The general form of a for loop is:
#       for LOOP_VARIABLE in SEQUENCE:
#           STATEMENTS  



def forExamples():  # using a range
    for i in range(5):
        print('i is now.......... %s' %(i))
    

    for key,val in my_dict.items():
        print("Key: " + key +"\t\tValue: " + str(val))

    for item in nationalParks: #enumerate
        print(item)
    
    for index,item in enumerate(nationalParks):
        print(str(index) + "\t" + item)
    
    
    

    
    
    
# A function is a block or organized, reusable code that is used to perform a sing
# related action
# The Python programming languages comes with a variety of built-in functions 
# example: print() 
    

# Importing Modules
    
# Modules are Python .py files that consist of Python code. Any Python file can be referenced as a module. 
# for example, a Python file called hello.py has the module name of hello that can be imported into other Python files, or used on the Python command line interpreter.
# Modules can define functions, classes, and variables that you can reference in other Python .py files or via the Python command line interpreter. 
# In Python, modules are accessed by using the import statement. When you do this, you execute the code of the module, keeping the scopes of the definitions so that your current file(s) can make use of these.
import random


for i in range(5):
    print(random.randint(1, 25))    

"""
It is possible to modify the names of modules and their functions within Python by using the as keyword.

You may want to change a name because you have already used the same name for something else in your program, another module you have imported also uses that name, 
or you may want to abbreviate a longer name that you are using a lot.
"""
import math as m


print(m.pi) #Within the program, we now refer to the pi constant as m.pi rather than math.pi
print(m.e)  #Within the program, we now refer to the pi constant as m.pi rather than math.pi

assignVariables()
