#functions go here

#Checks for name and if it's blank or not.
def not_blank(question, error_noname):
  valid = False
  
  while not valid:
    response = input(question)
    
    if response != "":
      return response
    else: 
      print(error_noname)

#Main routine goes here
name = not_blank("Name: ","Sorry, you have to have a name. Please enter your name.")

