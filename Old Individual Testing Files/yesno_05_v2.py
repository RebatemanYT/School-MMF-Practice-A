#yes/no function start

#Taking in 3 things: question, what are the valid responses, error message
def string_check(question, to_check, error):
  #error message
  
  valid = False
  while not valid:

    #ask question and put answer in lower case.
    response = input(question).lower()

    if response in to_check:
      return response
      
    else:
      for item in to_check:
        #Checks if the response is the first letter of an item in the list
        if response == item[0]:
          return item
          
    print(error)

#old code
"""
    if response == "yes" or "y":
      return "yes"
    elif response == "no" or "n" or "x":
      return "no"
    elif response == "xx" or "xxx":
      print("One x is also no. You put too many x's that we have to ask the question again.")
      continue
    else:
      print(error)
      continue
"""

#yes/no function end

#main routine goes here

for item in range(0,8):
  want_snacks = string_check("Do you want snacks? ", ["yes", "no", "x"], "Please answer with yes or no (or y or n).")
  
  if want_snacks == "x":
    #converting x to no
    want_snacks = "no"
    
  #output
  print("Output:", want_snacks, "\n")