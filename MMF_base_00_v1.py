#Import Statements

#functions goes here

#name_check function start
#Checks for name and if it's blank or not.
def not_blank(question, error):
  valid = False
  
  while not valid:
    response = input(question)
    #if name isn't blank, continue. If not, error and return to beginning.
    if response != "":
      return response
    else: 
      print(error)

# name_check function end

#age_check function start
def int_check(question, low_num, high_num):

  error = ("Please enter a whole number between {} " \
          "and {}, inclusive.".format(low_num, high_num))

  valid = False
  while not valid:
    
    #ask user for number and check if valid.
    try:
      response = int(input(question))
      
      #if interger is lower than lowest possible value, error. if interger is in correct range, good. if not, error.
      if response <= high_num:
        return response
      elif high_num < response:
        print("Sorry, it seems like you (likely) accidentally put too high of a number.")
        continue
      else:
        print(error)
      
    #if interger isn't recieved, display an error.
    except ValueError:
      print(error)
#age_check function end

#********** MAIN ROUTINE **********

#Set up dictionaries / Lists needed to hold data

#Ask user if they have used program before & show instructions if needed

#Loop to get info:

#Start of loop

#initalise loop so that it runs at least once
name = ""
count = 0
MAX_TICKET = 150

while name != "xxx" and count < MAX_TICKET:
  if count == MAX_TICKET - 1:
    #When 1 seat is left, don't say seats, say seat.
    print("You have {} seat "
       "left".format(MAX_TICKET - count))
  else:
    #In every other case, say seats.
    print("You have {} seats "
       "left".format(MAX_TICKET - count))

  #Get details
    #Get name (not blank)
    name = not_blank("Name: ","Sorry, you have to have a name. Please enter your name.")
  if name != "xxx":
    #Excluding the exit code from counting towards sold tickets.
    print("Name inputted.")

    #ask for age
    age = int_check("Age: ", 12, 130)
    #check if age is valid
    if age < 12:
      print("Sorry, you are too young for this movie.")
      continue
    #storing here for when needed the adding to the counter as if someone is too young, they would still count as a sold ticket.
    count += 1

if count == MAX_TICKET:
  #Lack of tickets = no more code running.
  print("You have ran out of available tickets.")
#Rest are correcting grammatical issues. 

elif MAX_TICKET - count == MAX_TICKET - 1 & MAX_TICKET - count == 1:
  #1 ticket sold and 1 ticket left.
  print("You have sold {} ticket.  \n"
       "You have {} ticket left."
       .format(count, MAX_TICKET - count))

elif MAX_TICKET - count == MAX_TICKET - 1:
  #1 ticket sold and multiple tickets left.
  print("You have sold {} ticket.  \n"
       "You have {} tickets left."
       .format(count, MAX_TICKET - count))

elif MAX_TICKET - count == 1:
  #Multiple tickets sold and 1 ticket left.
  print("You have sold {} tickets.  \n"
       "You have {} ticket left."
       .format(count, MAX_TICKET - count))

else:
  #Multiple tickets sold and multiple tickets left.
  print("You have sold {} tickets.  \n"
       "You have {} tickets left."
       .format(count, MAX_TICKET - count))

  #Calculate ticket price
  #Loop to ask for snacks
  #Calculate snack price
  #Ask for payment method
    #If needed, add surcharge.

#Calculate total sales and profit

#Output data to text file