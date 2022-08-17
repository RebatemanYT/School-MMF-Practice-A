#Import Statements
import re
import pandas

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

  error = ("Please enter a whole number between {} and {}, inclusive.".format(low_num, high_num))

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

#ticket_price function start
profit = 0 #starting profit is none
#Ticket numbers
def check_tickets(tickets_sold, ticket_limit):
  if tickets_sold == ticket_limit - 1:
    #When 1 seat is left, don't say seats, say seat.
    print("There is 1 seat left.")
  else:
    #In every other case, say seats.
    print("There is {} seats left.".format(ticket_limit - tickets_sold))

# Gets ticket price based on age
def get_ticket_price():

    # Get age (between 12 and 130
    age = int_check("Age: ", 12, 130)

    # check that age is valid...
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price
#ticket_price finction end

#********** MAIN ROUTINE **********

#Set up dictionaries / Lists needed to hold data

#Ask user if they have used program before & show instructions if needed

#Loop to get info:

#Start of loop

#initalise loop so that it runs at least once
name = ""
ticket_count = 0
MAX_TICKET = 2

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}


while name != "xxx" and ticket_count < MAX_TICKET:
  check_tickets(ticket_count, MAX_TICKET)
  name = not_blank("Name: ","Sorry, you have to have a name. Please enter your name.")
  if name != "xxx":
#Excluding the exit code from counting towards sold tickets etiher numerically or visually, along with skipping future steps.
    print("Name inputted.")
  else:
    break

  # Get ticket price based on age
  ticket_price = get_ticket_price()
  if ticket_price == "invalid ticket price":
    continue
  profit_made = ticket_price - 5
  profit += profit_made
    
  #storing here for when needed the adding to the counter as if someone is too young, they would still count as a sold ticket.
  ticket_count += 1
  # add name and ticket price to lists
  all_names.append(name)
  all_tickets.append(ticket_price)


# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

#Calculating ticket prices

if ticket_count == MAX_TICKET:
  #Lack of tickets = no more code running.
  print("You have ran out of tickets. You have made ${:.2f} in profit.".format(profit))
#Rest are correcting grammatical issues when exit code. 

elif MAX_TICKET - ticket_count == MAX_TICKET - 1 & MAX_TICKET - ticket_count == 1:
  #1 ticket sold and 1 ticket left.
  print("You have sold {} ticket. You have {} ticket left. You have made ${:.2f} in profit.".format(ticket_count, MAX_TICKET - ticket_count, profit))

elif MAX_TICKET - ticket_count == MAX_TICKET - 1:
  #1 ticket sold and multiple tickets left.
  print("You have sold {} ticket.  \n"
        "You have {} tickets left.  \n"
        "You have made ${:.2f} in profit." 
       .format(ticket_count, MAX_TICKET - ticket_count, profit))

elif MAX_TICKET - ticket_count == 1:
  #Multiple tickets sold and 1 ticket left.
  print("You have sold {} tickets.  \n"
        "You have {} ticket left.  \n"
        "You have made ${:.2f} in profit." 
       .format(ticket_count, MAX_TICKET - ticket_count, profit))

else:
  #Multiple tickets sold and multiple tickets left.
  print("You have sold {} tickets.  \n"
        "You have {} tickets left.  \n"
        "You have made ${:.2f} in profit." 
       .format(ticket_count, MAX_TICKET - ticket_count, profit))

  #Calculate ticket price - Done
  #Loop to ask for snacks - Done
  #Calculate snack price - Done
  #Ask for payment method
    #If needed, add surcharge.

#Calculate total sales and profit
