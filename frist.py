
"""def isleep(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def daysinmonth(year , month):
    if  month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isleep(year):
                return 29
            return 28
        else:
            return 30
def nextDay(year, month, day):
    
    dayes = daysinmonth(year , month)
    if day < dayes:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()

print(daysBetweenDates(2012, 2, 1, 2012, 3, 1))"""
# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.

# Let's store our counts in a list of length 11 
# with zeros filled in.

# We can multiply a list construct to create a list with the same
# elements n number of times.
count_list = [0] * 11

# Check that we have a list of length 11 with all 0 elements
print (count_list)

# We use this list to store our count of numbers 0 to 10 - take note 
# that total numbers 0 to 10 is 11. We can use the index number of
# each element to refer to the count of our target
# number. Our target number is actually the index of the list.
# For example, assume count_list looks like this:

count_list = [1,2,3,2,2,1,1,2,3,1,2]

# Let's print out the occurrences for the numbers 0, 4, 5, and 6
print (count_list[0])
print (count_list[4])
print (count_list[5])
print (count_list[6])

# Therefore, for our output, we want a count_list that looks like:
# [1,2,3,2,2,1,1,2,3,1,2]

# Here's our code that we coded before

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
# --------------------------------------------------------------------

# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5

count_list = [0] * 20
index = 0

# Write code here to loop through every number in random_list and
# update count_list appropriately


while index < len(random_list):
    count = 0 
    i = 0
    num = random_list[index]
    while i < len(random_list):
        if random_list[i] == num:
            count = count +1
        i = i +1
    count_list[index] = count
    index = index + 1
    
print ("number | occurrence")
i = 0
while i < len(random_list):
    print (' '*4 + str(random_list[i]) + ' | ' + str(count_list[i]))
    i = i+1



# Check the list we created
print (count_list)
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
print (sum(count_list))




