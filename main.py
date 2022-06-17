#import the functions from the other file
from AirlineFunctions import *

# This is where we declare the values for the tickets and discounts by age
coachTic = float(199)
firstClassTic = float(500)
discount = .20
seniorAge = 65
kidAge = 7
totalPrice = 0

#here are the variables for each currency value
bill100 = 100
bill50 = 50
bill20 = 20
bill10 = 10
bill5 = 5
bill1 = 1
quarters = .25
dimes = .10
nickels = .05
pennies = .01

#the array elements for each class of seats
firstClass = [["Open", "Open"], ["Open", "Open"], ["Open", "Open"], ["Open", "Open"]]
coach = [["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"], ["Open", "Open", "Open", "Open"]]

# This is where we need to do the inputs for passenger and ticket info into an array

numTravelers = 0
maxSeats = 48
minSeats = 0
row = 0
i = 1
prefClass = ("", "First Class", "Coach")
remainingSeats = maxSeats

#you are given a list of options at the very beginning.  Multiple if statements ensure proper usage of program
option = input("==== Hello and welcome to Chaffey Airlines. ====\n > Please type 't' to start traveler input, type 'p' to show airline seating arrangement, or type 'q' to quit reservation program at this time: ")
# while statement does not break until you either quit or fill all seats
while True:
  # typing 'p', at the beginning of the program, shows the seating plan
  if option == "p":
      #the tables are imported from the functions file
      print(firstTable(firstClass))
      print(coachTable(coach))

  #type 't' to start inputting traveler information and seat selecting
  elif option == "t":
    numTravelers = input("Please enter number of travelers: ")
    # we need to make sure the user inputs a number within the range of available seats
    while True:
      try:
        seats = int(numTravelers)
        if(seats > minSeats) and (seats <= remainingSeats):
          break
          #to start off, the flight starts with 48 seats.  The more seats are taken up, the less seats are available.  As long as a person inputs a number of people in their group that is within 1 to the remaining seats, this while loop will end
        else:
          numTravelers = input(" Please enter a two digit whole number of desired seats between 1 and "+ str(remainingSeats) + ": ")
      except ValueError:
        numTravelers = input(" Please enter a two digit whole number of desired seats between 1 and "+ str(remainingSeats) + ": ")
    # this is where we take the info for each traveller based on the number of travelers
    numTravelers = int(numTravelers)
    #this is the loop for getting the costs for the tickets.
    while i <= numTravelers:
      seatGranted = "N"
      travName = input("\nWhat is the traveler's first name: ")
      travLastName = input("What is the traveler's last name: ")
      travAge = input("Age of traveler: ")
      #the imported age function comes into play
      travAge = age(travAge)
      youPrefClass = input("Preferred Class- First Class [1] or Coach [2]: ")
      while seatGranted == "N":
        #you only have the options 1 and 2.  If ANYTHING else is inputted, you will be asked once again to choose a class
        #Details for First Class
        if youPrefClass == "1":
            print(firstTable(firstClass))
            # Now the traveler will select which first class row to choose from
            # here is where we manipulate the array
            while True:
              rowSelect = input("Which row will you choose? 1-4: ")
              #the imported First Class row function comes into play
              row = firstRows(rowSelect)
              rowSub = row - 1
              # Traveler will now need to choose a first class seat within row selected
              seat = input("Which seat in that row will you choose? A or B: ")
              #this makes sure you type either capital A or capital B
              while seat != "A" and seat != "B":
                seat = input("Please choose a seat from either A or B: ")
              if seat == "A":
                seatSub = 0
              elif seat == "B":
                seatSub = 1
              if firstClass[rowSub][seatSub] == "Open":
                firstClass[rowSub][seatSub] = travName
                print(" Seat granted.\n")
                seatGranted = "Y"
                break
              #if the row and seat subs equal an array element that says anything other than open, it will restart the selection process
              elif firstClass[rowSub][seatSub] != "Open":
                print(" Please choose another seat.\n")
                youPrefClass = input("Preferred Class- First Class [1] or Coach [2]: ")
                break
        #after seat has been selected, age of the traveler will be calculated to determine price of first class ticket
        if youPrefClass == "1" and seatGranted == "Y":
            priceTic = firstClassTic
            #if age is below 7 or over 65, a discount is applied
            if travAge <= kidAge or travAge >= seniorAge:
              priceAge = priceTic - (priceTic * discount)
              print(">>Discount applied.")
              break
              #otherwise you get the normal prices ticket
            elif travAge > kidAge and travAge < seniorAge:
              priceAge = priceTic
              break
          #Details for Coach
        elif youPrefClass == "2":
            print(coachTable(coach))
            # Now the traveler will select which coach row to choose from
            # here is where we manipulate the array
            while True:
              rowSelect = input("Which row will you choose? 1-10: ")
              #the imported Coach row function comes into play
              row = coachRows(rowSelect)
              rowSub = row - 1
              # Traveler will now need to choose a coach seat within row selected
              seat = input("Which seat in that row will you choose? A, B, C, or D: ")
              #this makes sure you type either capital A, capital B, capital C, or capital D
              while seat != "A" and seat != "B" and seat != "C" and seat != "D":
                seat = input("Please choose a seat from either A, B, C, or D: ")
              if seat == "A":
                seatSub = 0
              elif seat == "B":
                seatSub = 1
              elif seat == "C":
                seatSub = 2
              elif seat == "D":
                seatSub = 3
              if coach[rowSub][seatSub] == "Open":
                coach[rowSub][seatSub] = travName
                print(" Seat granted.\n")
                seatGranted = "Y"
                break
              #if the row and seat subs equal an array element that says anything other than open, it will restart the selection process
              elif coach[rowSub][seatSub] != "Open":
                print(" Please choose another seat.\n")
                youPrefClass = input("Preferred Class- First Class [1] or Coach [2]: ")
                break
        #after seat has been selected, age of the traveler will be calculated to determine price of coach ticket
        if youPrefClass == "2" and seatGranted == "Y":
            priceTic = coachTic
            #if age is below 7 or over 65, a discount is applied
            if travAge <= kidAge or travAge >= seniorAge:
              priceAge = priceTic - (priceTic * discount)
              print(">>Discount applied.")
              break
            #otherwise you get the normal prices ticket
            elif travAge > kidAge and travAge < seniorAge:
              priceAge = priceTic
              break
          #program makes sure you enter 1 or 2 only
        elif youPrefClass != "1" and youPrefClass != "2":
              youPrefClass = input("Please choose Preferred Class- First Class [1] or Coach [2]: ")
      #receipt information for traveler info and selection prints out
      print(" Traveler", travName, travLastName)
      print(" Traveling", prefClass[int(youPrefClass)] + ": Row", str(row) + ", Seat", seat)
      print(" General Ticket price: $%6.2f" % (priceAge))
      totalPrice = totalPrice + priceAge
      remainingSeats = remainingSeats - 1
      i = i + 1
    #This is where we checkout and make change based on total
    print("\nPlease review your seating details.")
    print(firstTable(firstClass))
    print(coachTable(coach))
    #program needs to add sales tax
    totalPrice = totalPrice + (totalPrice * 0.09)
    print("Total cost of ticket(s), with sales tax, will be $%6.2f." % (totalPrice))
    #now we will calculate how much the passenger(s) will pay and what the change will be.  a function from the other file is called for each denomination
    while True:
      bills100 = input (" Enter number of $100 bills: ")
      bills100 = money(bills100, bill100)
      bills50 = input (" Enter number of $50 bills: ")
      bills50 = money(bills50, bill50)
      bills20 = input (" Enter number of $20 bills: ")
      bills20 = money(bills20, bill20)
      bills10 = input (" Enter number of $10 bills: ")
      bills10 = money(bills10, bill10)
      bills5 = input (" Enter number of $5 bills: ")
      bills5 = money(bills5, bill5)
      bills1 = input (" Enter number of $1 bills: ")
      bills1 = money(bills1, bill1)
      quarter = input (" Enter number of quarters: ")
      quarter = money(quarter, quarters)
      dime = input(" Enter number of dimes: ")
      dime = money(dime, dimes)
      nickel = input (" Enter number of nickles: ")
      nickel = money(nickel, nickels)
      penny = input (" Enter number of pennies: ")
      penny = money(penny, pennies)
      #all of the cash denominations enter will be totaled up
      totalPaidAmt = float((bill100 * bills100) + (bills50 *bill50) + (bills20 * bill20)+ (bills10 * bill10) + (bill5 * bills5) + (bills1* bill1) + (quarters* quarter)+ (dimes * dime) + (nickels * nickel) + (penny * pennies))
      #if you didn't pay enough to cover your balance, you will have to restart
      if totalPaidAmt < totalPrice:
        print("You are attempting to pay with $%6.2f" % (totalPaidAmt))
        print("That is an insufficient amount.  Please try again. Remember your total due is $%6.2f" % (totalPrice))
      elif totalPaidAmt >= totalPrice:
        break

    print ("Total paid amount: $%6.2f" % (totalPaidAmt))
    changeAmt = (totalPaidAmt - totalPrice)
    print ("Total change: $%.2f" % (changeAmt))
    print("Thank you and enjoy your flight!")

  # If no travelers are input into the flight yet, Changing Seats is not available yet
  if option == "c" and remainingSeats == maxSeats: 
    print("__This is not a viable option at this time.__")
  
  # This is where we let passengers make changes to array by typing 'c', after at least one person is booked on the flight
  elif option == "c" and remainingSeats < maxSeats: 
      #you will start off by choosing which class you want to find passenger in
      youPrefClass = input("Which class is passenger in?- First Class [1] or Coach [2]: ")
      seatOpen = "N"
      while seatOpen == "N":
          #you only have the options 1 and 2.  If ANYTHING else is inputted, you will be asked once again to choose a class
          #Details for First Class
          if youPrefClass == "1":
            print(firstTable(firstClass))
            # enter row that passenger is currently in
            # here is where we manipulate the array
            while True:
              rowSelect = input("Which row is passenger in? 1-4: ")
              #the imported First Class row function comes into play
              row = firstRows(rowSelect)
              rowSub = row - 1
              # enter seat in which passenger is currently in
              seat = input("Which seat in that row is passenger in? A or B: ")
              #this makes sure you type either capital A or capital B
              while seat != "A" and seat != "B":
                seat = input("Please choose a seat from either A or B: ")
              if seat == "A":
                seatSub = 0
              elif seat == "B":
                seatSub = 1
                #if seat does not say open, passenger will now be taken out of it
              if firstClass[rowSub][seatSub] != "Open":
                traveName = firstClass[rowSub][seatSub]
                firstClass[rowSub][seatSub] = "Open"
                print(" Seat taken from " + travName + ".\n")
                seatOpen = "Y"
                break
              #if the row and seat subs equal an array element that says open, it will restart the selection process
              elif firstClass[rowSub][seatSub] == "Open":
                print(" Please choose another seat.\n")
                youPrefClass = input("Which class is passenger in?- First Class [1] or Coach [2]: ")
                break
          elif youPrefClass == "2":
            print(coachTable(coach))
            # enter row that passenger is currently in
            # here is where we manipulate the array
            while True:
              rowSelect = input("Which row is passenger in? 1-10: ")
              #the imported Coach row function comes into play
              row = coachRows(rowSelect)
              rowSub = row - 1
              # enter seat in which passenger is currently in
              seat = input("Which seat in that row is passenger in? A, B, C, or D: ")
              #this makes sure you type either capital A, capital B, capital C, or capital D
              while seat != "A" and seat != "B" and seat != "C" and seat != "D":
                seat = input("Please choose a seat from either A, B, C, or D: ")
              if seat == "A":
                seatSub = 0
              elif seat == "B":
                seatSub = 1
              elif seat == "C":
                seatSub = 2
              elif seat == "D":
                seatSub = 3
              if coach[rowSub][seatSub] != "Open":
                travName = coach[rowSub][seatSub]
                coach[rowSub][seatSub] = "Open"
                print(" Seat taken from " + travName + ".\n")
                seatOpen = "Y"
                break
              #if the row and seat subs equal an array element that says anything other than open, it will restart the selection process
              elif coach[rowSub][seatSub] == "Open":
                print(" Please choose another seat.\n")
                youPrefClass = input("Preferred Class- First Class [1] or Coach [2]: ")
                break
          #program makes sure you enter 1 or 2 only
          elif youPrefClass != "1" and youPrefClass != "2":
              youPrefClass = input("Please choose Preferred Class- First Class [1] or Coach [2]: ")
      #now passenger is removed from origina; seat, passenger will choose new seat
      newPrefClass = input("New Preferred Class- First Class [1] or Coach [2]: ")
      seatGranted = "N"
      while seatGranted == "N":
        #you only have the options 1 and 2.  If ANYTHING else is inputted, you will be asked once again to choose a class
        #Details for First Class
        if newPrefClass == "1":
            print(firstTable(firstClass))
            # Now the traveler will select which first class row to choose from
            # here is where we manipulate the array
            while True:
              rowSelect = input("Which row will you choose? 1-4: ")
              #the imported First Class row function comes into play
              row = firstRows(rowSelect)
              rowSub = row - 1
              # Traveler will now need to choose a first class seat within row selected
              seat = input("Which seat in that row will you choose? A or B: ")
              #this makes sure you type either capital A or capital B
              while seat != "A" and seat != "B":
                seat = input("Please choose a seat from either A or B: ")
              if seat == "A":
                seatSub = 0
              elif seat == "B":
                seatSub = 1
              if firstClass[rowSub][seatSub] == "Open":
                firstClass[rowSub][seatSub] = travName
                print(" Seat granted.\n")
                seatGranted = "Y"
                #if passenger was originally in coach, they will have to pay an upcharge for going to First Class
                if youPrefClass == "2":
                  upgrade = 300
                  print("Original Class was Coach.  Upgrade to First Class is $%6.2f" % (upgrade))
                  while True:
                    bills100 = input (" Enter number of $100 bills: ")
                    bills100 = money(bills100, bill100)
                    bills50 = input (" Enter number of $50 bills: ")
                    bills50 = money(bills50, bill50)
                    bills20 = input (" Enter number of $20 bills: ")
                    bills20 = money(bills20, bill20)
                    bills10 = input (" Enter number of $10 bills: ")
                    bills10 = money(bills10, bill10)
                    bills5 = input (" Enter number of $5 bills: ")
                    bills5 = money(bills5, bill5)
                    bills1 = input (" Enter number of $1 bills: ")
                    bills1 = money(bills1, bill1)
                    quarter = input (" Enter number of quarters: ")
                    quarter = money(quarter, quarters)
                    dime = input(" Enter number of dimes: ")
                    dime = money(dime, dimes)
                    nickel = input (" Enter number of nickles: ")
                    nickel = money(nickel, nickels)
                    penny = input (" Enter number of pennies: ")
                    penny = money(penny, pennies)
                    #all of the cash denominations enter will be totaled up
                    totalPaidAmt = float((bill100 * bills100) + (bills50 *bill50) + (bills20 * bill20)+ (bills10 * bill10) + (bill5 * bills5) + (bills1* bill1) + (quarters* quarter)+ (dimes * dime) + (nickels * nickel) + (penny * pennies))
                    #if you didn't pay enough to cover your balance, you will have to restart
                    if totalPaidAmt < upgrade:
                      print("You are attempting to pay with $%6.2f" % (totalPaidAmt))
                      print("That is an insufficient amount.  Please try again. Remember your total due is $%6.2f" % (upgrade))
                    elif totalPaidAmt >= upgrade:
                      break
                  print ("Total paid amount: $%6.2f" % (totalPaidAmt))
                  changeAmt = (totalPaidAmt - upgrade)
                  print ("Total change: $%.2f" % (changeAmt))
                  print("Thank you and enjoy your flight!")
                break
              #if the row and seat subs equal an array element that says anything other than open, it will restart the selection process
              elif firstClass[rowSub][seatSub] != "Open":
                print(" Please choose another seat.\n")
                newPrefClass = input("Preferred Class- First Class [1] or Coach [2]: ")
                break
        elif newPrefClass == "2":
            print(coachTable(coach))
            # Now the traveler will select which coach row to choose from
            # here is where we manipulate the array
            while True:
              rowSelect = input("Which row will you choose? 1-10: ")
              #the imported Coach row function comes into play
              row = coachRows(rowSelect)
              rowSub = row - 1
              # Traveler will now need to choose a coach seat within row selected
              seat = input("Which seat in that row will you choose? A, B, C, or D: ")
              #this makes sure you type either capital A, capital B, capital C, or capital D
              while seat != "A" and seat != "B" and seat != "C" and seat != "D":
                seat = input("Please choose a seat from either A, B, C, or D: ")
              if seat == "A":
                seatSub = 0
              elif seat == "B":
                seatSub = 1
              elif seat == "C":
                seatSub = 2
              elif seat == "D":
                seatSub = 3
              if coach[rowSub][seatSub] == "Open":
                coach[rowSub][seatSub] = travName
                print(" Seat granted.\n")
                seatGranted = "Y"
                break
              #if the row and seat subs equal an array element that says anything other than open, it will restart the selection process
              elif coach[rowSub][seatSub] != "Open":
                print(" Please choose another seat.\n")
                newPrefClass = input("Preferred Class- First Class [1] or Coach [2]: ")
                break
      #program makes sure you enter 1 or 2 only
        elif youPrefClass != "1" and youPrefClass != "2":
          newPrefClass = input("Please choose Preferred Class- First Class [1] or Coach [2]: ")

  #if no one is in the flight, program can be shut down. break statement will stop the options loop and go to the very end of program
  if option == "q" and remainingSeats == maxSeats:
    break

  #if there is at least 1 person on the flight, program cannot be shut down
  elif option == "q" and remainingSeats < maxSeats:
    print("__This is not a viable option.__")

  #to prevent someone from not typing the options t, p, q, or c
  if option != "t" and option != "p" and option != "q" and option != "c":
    print("__This is not an option.__")

  #this is if you haven't inputting any travelers yet
  if remainingSeats == maxSeats:
    option = input("\n> Please type 't' to start traveler input, type 'p' to show airline seating arrangement, or type 'q' to quit reservation program at this time: ")
  #this is for when you have at least one traveler is input
  elif remainingSeats > minSeats and remainingSeats < maxSeats:
    option = input("\n> Please type 't' to go to traveler input, type 'p' to show airline seating arrangement, or type 'c' to change a reserved seat: ")
    #reset named constants
    i = 1
    totalPrice = 0
    seatGranted = "N"
  #if all seats are filled.  break statement will stop the options loop and go to the very end of program
  elif remainingSeats <= minSeats:
    break
  
#once all seats are filled:
if remainingSeats <= minSeats:
  print("\nFlight is full.")
  print(firstTable(firstClass))
  print(coachTable(coach))
#Whether you quit the program at the start or you filled all the seats in the flight:
print("\nHave a nice day!")
