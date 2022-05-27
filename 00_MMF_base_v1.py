#Import Statements

#functions goes here

#Checks for name and if it's blank or not.
def not_blank(question, error_noname):
  valid = False
  
  while not valid:
    response = input(question)
    #if name isn't blank, continue. If not, error and return to beginning.
    if response != "":
      return response
    else: 
      print(error_noname)

#********** MAIN ROUTINE **********

#Set up dictionaries / Lists needed to hold data

#Ask user if they have used program before & show instructions if needed

#Loop to get info:

  #Get name (not blank)
name = not_blank("Name: ","Sorry, you have to have a name. Please enter your name.")
  #Get age (between 12 and 130)
  #Calculate ticket price
  #Loop to ask for snacks
  #Calculate snack price
  #Ask for payment method
    #If needed, add surcharge.

#Calculate total sales and profit

#Output data to text file