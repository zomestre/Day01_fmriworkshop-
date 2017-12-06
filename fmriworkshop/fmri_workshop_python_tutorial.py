# -*- coding: utf-8 -*-
'''
Created on Tue Nov 28 17:48:40 2017
@author: Nichollette

This is a basic script for the fMRI workshop Python Basic Lesson
This is how you do a block comment
'''

# This is how you do individual comments




def makeList(print_list):
    
    
    nationalParks = ['Yosemite', 'Grand Canyon', "Zion", "Bryce", "Arches"]
    
    if print_list == True:
        print("Index 0 of National Parks list: " + nationalParks[0])
    
    return nationalParks 


def appendList(userInput):
    nationalParks.append(userInput)
    print(nationalParks)







def sortList():
    print(nationalParks)
    nationalParks.sort()
    print(nationalParks)




def makeDictionary(print_dict):
    
    # empty dictionary
    my_dict = {}

     # dictionary
    my_dict= {
        'Name' : 'Leo',
        'Species': 'Cat', 
        'Age': 7
        }
    
    if print_dict == True:
        
        print(my_dict)
        print("dict['Name']:", my_dict['Name'], "\ndict['Species']:", my_dict['Species'], "\ndict['Age']):", my_dict['Age'])
    
    return my_dict 
  






def dictionaryExamples(selection):
    if selection == "IF":
        if "Name" in my_dict: 
            print("TRUE")
    if selection == "Update":
        my_dict['Age'] = 8; # update Dictionary
        print("Updated dict['Age']", my_dict['Age'])
    if selection == "Add":
        my_dict['BloodType'] = 'A';  # Add new entry
        print(dict)
       
        
# compound statements

# if statement
# colon (:) is required, separates the HEADER from the BODY
# example:  
#       if BOOLEAN EXPRESSION:
#           STATEMENTS 

# The line after the colon must be indented - Python standard 4 spaces
# (==)


    
def ifExamples(choice):
        
   if choice == "variable":
       if 10 > 5:   #variableB is True: #  , 5 > 10
            print("Condition is TRUE. I am in the if block.")
       else:
           print("Condition is FALSE. I am in else block.")

   if choice == "list":
        if 'Yosemite' in nationalParks:
            print("Found 'Yosemite' in our list")
    

# The for loop processes each item in a sequence, so it is used with Python’s sequence data types - strings, lists, and tuples.
# The general form of a for loop is:
#       for LOOP_VARIABLE in SEQUENCE:
#           STATEMENTS  



def forExamples(choice):  # using a range
    if choice == "Range":
        for i in range(5):
            print('i is now.......... %s' %(i))
    
    if choice == "KV":
        for key,val in my_dict.items():
            print("Key: " + key +"\t\tValue: " + str(val))

    if choice == "NPI":
        for item in nationalParks: #enumerate
            print(item)
    
    if choice == "NPII":
        for index,item in enumerate(nationalParks):
            print(str(index) + "\t" + item)
    if choice == "Squares":
        sum = 0
        for num in squares:
            sum += num
        print("Sum of Squares list: " + str(sum))

    
    
    
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


#for i in range(5):
 #   print(random.randint(1, 25))    

"""
It is possible to modify the names of modules and their functions within Python by using the as keyword.

You may want to change a name because you have already used the same name for something else in your program, another module you have imported also uses that name, 
or you may want to abbreviate a longer name that you are using a lot.
"""
#import math as m


#print(m.pi) #Within the program, we now refer to the pi constant as m.pi rather than math.pi
#print(m.e)  #Within the program, we now refer to the pi constant as m.pi rather than math.pi






def print_variables():
     print("Integer: %d\n" % (variableI) +  "Float:  %d\n" % (variableF) 
        + "Boolean:  %s\n" %(variableB) + "String: %s" %(variableS))  




def main():

   go = True
   
   
    
   while go != False: 

        start_selection = input("Examples\n a. \t var - variable\n b. \t for \n c. \t dict \n d. \t if \n ENTER CHOICE: " )
        
        if start_selection == "a":
            print_variables()
        if start_selection == "b":
            for_choice = input("Enter List Example Choice: \n <Range, KV, NPI, NPII, Squares>: ")
            forExamples(for_choice)
        if start_selection == "c":
            dict_choice = input("Enter Dictionary Example Choice \n <IF, Update, Add>: ")
            dictionaryExamples(dict_choice)
        if start_selection == "d":
            if_choice = input("Enter If Example Choice \n <variable, list>: ")
            ifExamples(if_choice)
    
        go = input("Continue? ")
        #go =False 
        return go 





variableI = 100 # This is an Integer 
variableF= 100.30 # This is a Float 
variableB = False # This is a Boolean 
variableS = "fMRI Workshop 2017" # This is a String

squares = [1, 4, 9, 16]


nationalParks = makeList(False)
#x=False
my_dict = makeDictionary(False)
    
    

main()