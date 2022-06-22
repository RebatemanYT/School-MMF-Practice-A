#yes/no function start
def yesno (question):
  #error message
  error = "Please answer yes or no."
  
  valid = False
  while not valid:

    #ask question and put answer in lower case.
    response = input(question).lower()
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

#yes/no function end

#main routine goes here

for item in range(0,6):
  want_snacks = yesno("Do you want snacks? ")
  print("You have inputed a valid answer. To simplify code, we have converted your answer to", want_snacks, "so let's go to what your answer says to do. \n")