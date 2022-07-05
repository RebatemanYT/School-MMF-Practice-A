#yes/no function start

#valid snack list
valid_snacks = [
  ["popcorn", "p", "a"], #Popcorn
  ["m&m's", "mm", "m&ms", "m&m", "mm's", "mms", "chocolate", "m", "b"], #M&Ms
  ["pita chips", "pc", "p c", "pita", "chip", "chips", "c"], #Pita Chips
  ["water", "drink", "w", "d"], #Water
  ["xxx", "x", "e"] #Done - Used to exit loop
]
yn = [
  ["yes", "y"],
  ["no", "n", "x"]
]
#initalize ariables
snack_ok = ""
snack_list = ""
var_list = ""

#Taking in 3 things: question, what are the valid responses, error message
def string_check(question, to_check, error):
  #error message
  
  valid = False
  while not valid:

    #ask question and put answer in lower case.
    response = input(question).lower()

    if response in to_check:
      var_list == to_check[0].title()
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

#Want Snacks?
for item in range(0,8):
  want_snacks = string_check("Do you want snacks? ", yn, "Please answer with yes or no (or y or n).")
  
  if want_snacks == "x":
    #converting x to no
    want_snacks = "no"
    
  #output
  print("Output:", want_snacks, "\n")
  
  if want_snacks != "no":
    print("List of snack options: \n",
         "a. Popcorn \n",
         "b. M&Ms \n",
         "c. Pita Chips \n",
         "d. Water \n",
         "e. xxx (Replacement for 'done', continues past this point) \n")
    snack = string_check("What snacks do you want? ", valid_snacks, "Please refer to the list of snacks. \n")
    if snack != "xxx" or snack != "x" or snack != "e":
      print("Output:", snack, "\n")
    else:
      print("test 2")