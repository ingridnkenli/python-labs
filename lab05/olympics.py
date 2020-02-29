# File: olympics.py
# Author: Ingrid Nkenlifack
# Date: 2/26/18
# Section: 2
# E-mail: tz57818@umbc.edu
# Description: This program will print the olympic event choices

STOP = 0

def main():

    # list of Olympic events to vote on
    events = ["bobsledding", "figure skating", "skiing","snowboarding", "curling", "luge", "ice hockey"]

    # list all events in olympics numbered
    count = 0
    while count < len(events):
        print(count + 1,"-", events[count])
        count += 1

    #tally votes from favorite olympic events
    votes = [0, 0, 0, 0, 0, 0, 0]

    #ask for all favorite olympics.  choice corresponds to event # fav.
    choice = int(input("What is your favorite Olympic event?(Enter " + str(STOP) + ") to stop: "))

    #makes sure invalid choices are ignored
    if choice <= len(votes):
        votes[choice - 1 ] += 1

    #keeps asking user for all input not = 0
    while choice != STOP:
        choice = int(input("What is your favorite Olympic event?(Enter " + str(STOP) + " ) to stop): "))
        #makes sure invalid choices are ignored
        if choice > STOP and choice <= len(votes):
            votes[choice - 1] += 1
    
    
    #print out tally of fav events votes
    count = 0
    while count < len(votes):
        print(events[count], "has", votes[count], "votes.")
        count +=1 

        


main()
