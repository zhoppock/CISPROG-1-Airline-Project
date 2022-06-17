#the following two functions print the seating arrangements for first class and coach, respectively
#for each of these functions, the group variable adds each line as a single string value so the function can correctly product the table output when called in the main program
def firstTable(f):
  group = ""
  # r increments to define the number of each row
  r = 1
  group += "\n\t\t========= First Class ======== \n"
  group += "      |    Seat A    |    Seat B    |\n"
  #the for loop prints each row with it's open seats, with 12 character spaces per seat
  for item in f:
    group += "Row " + str(r) + " | " + item[0] + " "*(12-len(item[0])) + " | " + item[1] + " "*(12-len(item[1])) + " |\n"
    r += 1
  return group

def coachTable(c):
  group = ""
  # r increments to define the number of each row
  r = 1
  group += "\n\t\t========= Coach Class ======== \n"
  group += "      |    Seat A    |    Seat B    |    Seat C    |    Seat D    |\n"
  #the for loop prints each row with it's open seats, with 12 character spaces per seat.  To make sure Row 10 doesn't push the table out of line, IF statements are implemented with slight different printing instructions
  for item in c:
    if r < 10:
      group += "Row " + str(r) + " | " + item[0] + " "*(12-len(item[0])) + " | " + item[1] + " "*(12-len(item[1])) + " | " + item[2] + " "*(12-len(item[2])) + " | " + item[3] + " "*(12-len(item[3])) + " |\n"
    if r == 10:
      group += "Row " + str(r) + "| " + item[0] + " "*(12-len(item[0])) + " | " + item[1] + " "*(12-len(item[1])) + " | " + item[2] + " "*(12-len(item[2])) + " | " + item[3] + " "*(12-len(item[3])) + " |\n"
    r += 1
  return group

# all of the functions below make sure that only a whole number is inputted

#need to make sure the age of a person is a number from 0 and above
def age(age):
  while True:
    try:
      ageOf = int(age)
      if ageOf >= 0:
        break
        #the age inputted is 0 or above so the function will end
      else:
        age = input("Please enter age from range 0 and above: ")
    except ValueError:
      age = input("Please enter age from range 0 and above: ")
  return ageOf

# functions that make sure the user chooses the appropriate available rows available
def firstRows(row):
  while True:
    try:
      rows = int(row)
      if rows > 0 and rows < 5:
        break
        #the first class row inputted is 1 to 4 so the function will end
      else:
        row = input("Please choose a row from 1-4: ")
    except ValueError:
      row = input("Please choose a row from 1-4: ")
  return rows

def coachRows(row):
  while True:
    try:
      rows = int(row)
      if rows > 0 and rows < 11:
        break
        #the coach row inputted is 1 to 4 so the function will end
      else:
        row = input("Please choose a row from 1-10: ")
    except ValueError:
      row = input("Please choose a row from 1-10: ")
  return rows

#this will make sure an appropriate number of bills or coins are input, depending on the cash denomination put in the parameter
def money(amount, denomination):
  while True:
    try:
      cash = int(amount)
      if cash >= 0:
        break
        #the cash ammount inputted is 0 or above so the function will end
      else:
        print("For the denomination", str(denomination), end = "")
        amount = input(", please enter amount from range 0 and above: ")
    except ValueError:
      print("For the denomination", str(denomination), end = "")
      amount = input(", please enter amount from range 0 and above: ")
  return cash