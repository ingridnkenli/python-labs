# File: super.py
# Author: Ingrid Nkenlifack
# Date: 2/12/2018
# Section: 02
# E-mail: tz57818@umbc.edu
# Description: Use decision structures to offer advice about a super powered person
#


def main():

    job = input("Are you a hero or villain?")

    if job == "hero":
        saved = int(input("How many people have you saved?"))
        if saved >= 100:
            print("Wow, great job saving the city!")
        elif saved > 10:
            print("Sounds like you're making a difference!")
        else:
            print("Go on more patrols!")
    else:
        name = input("What is your name?")
        print(name, "sounds pretty evil!")

    


main()
