# File:        names.py
# Started:     by Brianna Richardson (& Dr. Gibson)
# Author:      Ingrid Nkenlifack
# Date:        3/5/18
# Section:     2
# E-mail:      tz57818@umbc.edu
# Description: This file contains python code that uses functions to allow 
#              a user to get information about a list of names entered.

SENTINEL = "-1"

###################################################################
# printList() prints out a list, showing the index of each element
# Input:      theList; a list of any types of variables
# Output:     None
def printList(theList):
    #---------------------------------------------------------#
    index = 0
    while index < len(theList):
        print("At index ",index, "the name is ",theList[index])
        index += 1

    

######################################################################
# printMinStr() prints the string with the minimum length from a list
# Input:        theList; a list of strings
# Output:       None

def printMinStr(theList):
    
    index = 0
    listMin = theList[0]

    while index < len(theList):
        if len(theList[index]) < len(listMin):
            listMin = theList[index]
        else:
            listMin = listMin
        index += 1

    print("The shortest string in the list is ", listMin)


######################################################################
# printMaxStr() prints the string with the maximum length from a list
# Input:        theList; a list of strings
# Output:       None

def printMaxStr(theList):
    #--------------------------------------------------------------#
    index = 0
    listMax = theList[0]

    while index < len(theList):
        if len(theList[index]) > len(listMax):
            listMax = theList[index]
        else:
            listMax = listMax
        index += 1

    print("The longest string in the list is ", listMax)
    

def main():

    nameList = []

    msg = "Enter a name (or " + SENTINEL + " to quit): "

    name = input(msg)

    # ask the user for names until they choose to exit
    while name != SENTINEL:
        # check beforehand, so we only save valid names
        nameList.append(name)

        name = input(msg)


    # call the print function      
    printList(nameList)

    # print out the minimum and maximum length names
    printMinStr(nameList)
    printMaxStr(nameList)

main()
