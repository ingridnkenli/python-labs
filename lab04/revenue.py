# File: revenue.py
# Author: Ingrid Nkenlifack
# Date: 2/19/18
# Section: 2
# E-mail: tz57818@umbc.edu
# Description: The program you are writing will be used to find the minimum and maximum in a list of company revenues


def main():

    numRevenue = int(input("How many revenues would you like to enter?"))
    count = 1

    while numRevenue <= 0:
        print("You must enter a number greater than zero.")
        numRevenue = int(input("How many revenues would you like to enter?"))
    
    firstRevenue = float(input("Enter a revenue."))

    minRevenue = firstRevenue
    maxRevenue = firstRevenue

    while count < numRevenue:
        count += 1
        newRevenue = float(input("Enter a revenue:"))
        if newRevenue > maxRevenue:
            maxRevenue = newRevenue
        if newRevenue < minRevenue:
            minRevenue = newRevenue
        

    print("The minimum revenue entered was ", minRevenue)
    print("The maximum revenue entered was ", maxRevenue)




main()
