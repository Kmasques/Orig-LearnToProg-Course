#Ask user if they want a sandwich
hungry = raw_input("Would you like a sandwich? Type Y for yes: ")

#If user wants a sandwich=="Y":
if hungry.upper () == "Y":
    
    #Serve sandwiches while user is hungry
    while hungry.upper () == "Y":
        
        #Gather ingredients, print message and serve sandwich
        print "Getting bread, peanut butter, and jelly . . ."
        print "I's Peanut Butter and Jelly time!"
        
        #Ask if user is still hungry
        hungry = raw_input("Would you like another sandwich?: ")
        
    #If they are full, print message thanking them
    print "Thanks for coming, hope you enjoyed our sanndwiches."
        
#If user does not want a sandwich
else: 
    #Ask user to come back when they are hungry
    print "Come back again when you are hungry"
