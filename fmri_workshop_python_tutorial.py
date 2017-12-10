# -*- coding: utf-8 -*-
'''

@author: Nichollette Acosta

This is a basic script for the fMRI workshop Python Basic Lesson
This is how you do a block comment
'''

# This is how you do individual comments

# A function is a block or organized, reusable code that is used to perform a sing
# related action
# The Python programming languages comes with a variety of built-in functions 
# example: print() 
    

# Importing Modules
    
# Modules are Python .py files that consist of Python code. Any Python file can be referenced as a module. 
# for example, a Python file called hello.py has the module name of hello that can be imported into other Python files, or used on the Python command line interpreter.
# Modules can define functions, classes, and variables that you can reference in other Python .py files or via the Python command line interpreter. 
# In Python, modules are accessed by using the import statement. When you do this, you execute the code of the module, keeping the scopes of the definitions so that your current file(s) can make use of these.
#import random



"""
It is possible to modify the names of modules and their functions within Python by using the as keyword.

You may want to change a name because you have already used the same name for something else in your program, another module you have imported also uses that name, 
or you may want to abbreviate a longer name that you are using a lot.
"""

## Lists: mutable(changeable) sequences of object references accessed by offset(position)
## They are unordered tables that map key to values. 
# the makeList() function shows how to assign lists to variables
 


def assignVariables():
    variableI = 100 # This is an Integer 
    global variableF
    variableF= 100.30 # This is a Float 
    global variableB
    variableB = False # This is a Boolean 
    global variableS
    variableS = "fMRI Workshop 2017" # This is a String



def makeList():
    
    # make an empty list -- the list is local 
    emptyList = []
    
    # make a list of Strings
    global nationalParks
    nationalParks = ['Yosemite', 'Grand Canyon', "Zion", "Bryce", "Arches"]

    # make a list of integers
    global intList 
    intList = [ 10, 60, 30, 40, 90]
    
    # make a mixed list
    mixedList = [ 100, 'Dr. Pepper', 75.25, True ]
    
    return mixedList


# the listExamples() function shows various list manipulation examples 
    
def listExamples(park):
    newpark = park
    
    # add, or 'append', an item to the end of a list 
    # --add item explicitly
    nationalParks.append("Yellowstone")  
    intList.append(50)
    
    # -- add item through a variable
    nationalParks.append(newpark)
    
    print(nationalParks)

    # sort a list 
    nationalParks.sort()
    intList.sort()
    
    # check the length of your list 
    len(nationalParks)
    
    # access the first item in the list
    nationalParks[0]
    
    # access the last item in the list
    nationalParks[-1] 
    
    # use a method called 'slicing' to access the list
    nationalParks[4]
    # -- get items after index 4
    nationalParks[4:]
    # -- get items before index 4
    nationalParks[:4]
    # -- get items between index 2 and 5 
    nationalParks[2:5]
    
    # delete item 4 (index 3) from list 
    del nationalParks[3]
    
    
    

## Dictionaries: mutable(changeable) mappings of object references accessed by key.

    
def makeDictionary():
    
    # make an empty dictionary
    empty_dict = {}

     # dictionary
    global animal_dict 
    animal_dict= {
        'Name' : 'Leo',
        'Species': 'Cat', 
        'Age': 7
         
        }
    
  
def dictionaryExamples():
    
    # get dictionary keys
    animal_dict.keys()
    # get dictionary values
    animal_dict.values()
    # get dictionary items 
    animal_dict.items()
    
    # returns true if dictionary has key "name" in it, false otherwise
    "Name" in animal_dict
          
    # update value of dictionary 
    animal_dict['Age'] = 8; 
    # add new entry to dictionary 
    animal_dict['BloodType'] = 'A';  # Add new entry
    
     
## The if statement: selects from one or more actions(statement blocks)
# colon (:) is required, separates the HEADER from the BODY
# example: 
#            if test:
#                statement 
#            [elif test:
#               statement]*
#            [else:
#                statement]
    
#           ***The line after the colon must be indented - Python standard 4 spaces



def ifExamples():
    
    # Example of using an if-statement on a list:
    if 'Yosemite' in nationalParks:
        print("Found 'Yosemite' in our list")
    
    # Example of an if-else statement with a comparison operator 
    if 10 > 5:  
        print("Condition is TRUE. I am in the if block.")
    else:
        print("Condition is FALSE. I am in else block.")

    # Example of if-elif-else statement
    stoplight = "red"
    if stoplight == "green":
        print("go")
    elif stoplight == "red":
        print("stop")
    else:
        print("yield")
    

## The for loop: a sequence(or other iterable) iteration that assings items in SEQUENCE to LOOP_VARIABLE
## and runs the STATEMENT
## example:
        # The general form of a for loop is:
        #               for LOOP_VARIABLE in SEQUENCE:
        #                   STATEMENTS  

def forExamples():  
    
    # for loop using a range method 
    for i in range(5):
        print('i is now.......... %s' %(i))
    
    
    # for loop on a list
    for item in nationalParks: 
        print(item)
        
    # for loop on a list, using enumerate() method to get index 
    for index,item in enumerate(nationalParks):
        print(str(index) + "\t" + item)
    
    # for loop on a dictonary -- notice how simple for loop retrieves keys only 
    for item in animal_dict:
        print(item)
        
    # for loop on a dictionary -- using values() to get only values
    for item in animal_dict.values():
        print(item)
        
    # for loop on a dictionary -- using items() to get key and value
    for key,val in animal_dict.items():
        print(key, val)

    
    
    # using a for loop to sum values in a list: 
    sum = 0
    for num in intList:
        sum += num
        print(sum)


# The main() function 
# Python does not have a main entry point, it executes the source file line by line. Having 
# a main() funciton is good practice.
        
def main():
    
    # call functions 
    assignVariables()
    makeDictionary()

    # return from a function
    mixed_list = makeList()
    print(mixed_list)

    # call a function with a variable
    # park = "Death Valley"
    listExamples("Death Valley")
    
    ifExamples()
    forExamples()
    dictionaryExamples()
    
   
# delcare a global variable 
variableI = 0 

    
# first function to run - calls main 
main()
