#functions goes here

def int_check(question, low_num, high_num):

  error = ("Please enter a whole number between {} " \
          "and {}, inclusive. \n".format(low_num, high_num))

  valid = False
  while not valid:
    
    #ask user for number and check if valid.
    try:
      response = int(input(question))
      
      #if interger is lower than lowest possible value, error. if interger is in correct range, good. if not, error.
      if response <= high_num:
        return response
      elif high_num < response:
        print("Sorry, it seems like you accidentally put too high of a number.")
        continue
      else:
        print(error)
      
    #if interger isn't recieved, display an error.
    except ValueError:
      print(error)

#main routine goes here

#ask for age
age = int_check("Age: ", 12, 130)
