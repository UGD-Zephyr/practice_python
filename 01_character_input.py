# Programmer: Per Stoor
# Date: 2022-09-24
# last changed: 2022-09-24
# Type of program: Practicing character input in python.

def hundredYearBirthday(name, age, currentYear, ageToHundred, hundredYear):
    """
    This function prints out
    what year you will be a
    hundred years old.
    """

    print("Your name is", name, end=" ")
    print("and your age is", age)
    print("You will be a hundred years old in the year", hundredYear)


name            = input("name:")
age             = int(input("age:"))
currentYear     = 2022
ageToHundred    = 100 - age 
hundredYear     = ageToHundred + currentYear 
loopCounter1    = int(0)

hundredYearBirthday(name, age, currentYear, ageToHundred, hundredYear)

amountOfCopies = int(input("amount of copies:"))

for loopCounter1 in amountOfCopies:
    hundredYearBirthday(name, age, currentYear, ageToHundred, hundredYear)
