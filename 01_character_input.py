# Programmer: Per Stoor
# Date: 2022-09-24
# last changed: 2022-09-24
# Type of program: Practicing character input in python.

import datetime

def hundredYearBirthday(name, age, currentYear, ageToHundred, hundredYear):
    """
    This function prints out
    what year you will be a
    hundred years old.
    """

    print("----------------------------")
    print("Your name is", name, end=" ")
    print("and your age is", age)
    print("You will be a hundred years old in the year", hundredYear)
    print("----------------------------")

pass

name            = input("name:")
age             = int(input("age:"))
today           = datetime.date.today()
currentYear     = today.year
ageToHundred    = 100 - age 
hundredYear     = ageToHundred + currentYear 
loopCounter1    = int(0)
yearlyBirthday = input("Did you already celebrate your birhtday this year? y/n: ")

if yearlyBirthday == "n" or yearlyBirthday == "N" or yearlyBirthday == "no" or yearlyBirthday == "NO" or  yearlyBirthday == "No":
    hundredYear = (hundredYear - 1)

hundredYearBirthday(name, age, currentYear, ageToHundred, hundredYear)
amountOfCopies = int(input("amount of copies:"))

while (amountOfCopies > 0):

    hundredYearBirthday(name, age, currentYear, ageToHundred, hundredYear)
    amountOfCopies = (amountOfCopies - 1)
