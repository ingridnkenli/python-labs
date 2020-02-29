# File:    spending.py
# Started: by Dr. Gibson
# Author:  Ingrid Nkenlifack
# Date:    3/26/18
# Section: 2
# E-mail:  tz57818@umbc.edu
# Description:
#   This file contains python code that tallies a list
#   of expenditures (both by category and in total).


# the category title is the first element of each list
CATEGORY_TITLE = 0

#-------------------------------------------------------------------------
# printSpending() prints the expenditures in all spending categories
# Input:          spendingList, a 2D list holding the expenditures
# Output:         None
#--------------------------------------------------------------------------
def printSpending(spendingList):

    print("\nSpending:")
    print("---------------")
    index = 0

    #loop through each category of expenditures
    while index < len(spendingList):

        # print out the category title with a colon afterwards
        print(spendingList[index][CATEGORY_TITLE], ":" , end= "\t")


        index2 = 1
        while index2 < len(spendingList[index]):
            print(spendingList[index][index2], end ="\t")
            index2 += 1
        index += 1
        print()

#------------------------------------------------------------------
# tallySpending() Finds total amount of money spent this month
# Input:          spending;   2D list of expenditures
# Output:         totalSpent; float, the total expenditures
#                (Also prints out total of each category.)
#-----------------------------------------------------------------
def tallySpending(spending):

    totalSpent = 0

    categoryIndex = 0      # used to access each spending category

    # loop through the entire list of expenditures
    while categoryIndex < len(spending):
        
        # tally the total expenditures for this individual category
        categoryTotal = 0
        purchaseIndex = 1  # used to access each individual purchase
                           # (starts at 1 to skip the category title)
        while purchaseIndex < len(spending[categoryIndex]):           

            categoryTotal += spending[categoryIndex][purchaseIndex]

            purchaseIndex += 1
        # print the total expenditures for this category
        print("In category", spending[categoryIndex][CATEGORY_TITLE], \
                  "\t$" + str(categoryTotal), "was spent")
        
        categoryIndex += 1
        # add to running total of all expenditures
        totalSpent    += categoryTotal

    # return the total amount of expenditures
    return totalSpent



def main():
    spending = [['EAT OUT', 15.86, 42.79, 13.8 ,  9.16,  9.16,  5.42, 49.3], \
                    ['VEHICLE',    25.68, 89   ,  7.99, 23.11             ], \
                    ['GROCERIES',  54.33, 30.27,  5.88, 40.71             ], \
                    ['UTILITIES', 165.31, 17.32                           ], \
                    ['PERSONAL',   25   , 14.91, 40.52                    ], \
                    ['ENTERTAIN',  15.66, 13   ,  5.99, 33.04             ], \
                    ['PET CARE',  100   , 13.91, 48.98, 17.22, 42.45      ], \
                    ['RENTING',  1300                                     ]]

    
    # print the current spending list
    printSpending(spending)
    print("\n")
    
    #prints $ spent for each category
    tallySpending(spending)

    #stores total $ spent in totalSpent 
    totalSpent = tallySpending(spending)
    print("\nYou spent a total of \t$" + str(totalSpent), "this month")
main()
