#functions go here

def: not_blank(question):
  valid = False
  while not valid:
    response = input(question)
    if response != "":
      return response
    else: 
      print("Error <Sorry, you have to have a name. Please enter your name.>")

#Main routine goes here
  name = not_blank("Name: ")