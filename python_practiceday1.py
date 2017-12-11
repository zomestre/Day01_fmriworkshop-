"""
fMRI Workshop 2017 UNC Chapel Hill

Basic Python Practice

"""


# Task
#Store a string to a variable and print that variable.

# your code here

###########################################################################################################################


#Task
#Given an integer, , perform the following conditional actions:

#    If n is odd, print Weird
#    If n is even and in the inclusive range of to , print Not Weird
#    If n is even and in the inclusive range of to , print Weird
#    If n is even and greater than , print Not Weird

n = int(input())

# your code here


###########################################################################################################################
#Task 
#Read two integers from STDIN and print three lines where:

#    The first line contains the sum of the two numbers.
#    The second line contains the difference of the two numbers (first - second).
#    The third line contains the product of the two numbers.

a = int(input())
b = int(input())

# your code here



###########################################################################################################################
#Task
#You are given the year, and you have to write a function to check if the year is leap or not.

#Note that you have to complete the function and remaining code is given as template.


"""We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

"""
def is_leap(year):
    leap = False
    
    # your code here 
    
    
    return leap

year = int(input())
print(is_leap(year))

###########################################################################################################################
# Task
# Find 3 different libraries to import and run 2 examples from each library 
 
 
