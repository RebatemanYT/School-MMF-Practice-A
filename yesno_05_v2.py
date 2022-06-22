#yes/no function start
def string_check(question):
  #error message
  error = "Please answer with yes or no (or y or n)."
  
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

for item in range(0,6):
  want_snacks = string_check("Do you want snacks? ", ["yes", "no", "x"])
  
  if want_snacks == "x":
    #converting x to no
    want_snacks = "no"
  
  print("You have inputed a valid answer. To simplify code, we have converted your answer to", want_snacks, "so let's go to what your answer says to do. \n")