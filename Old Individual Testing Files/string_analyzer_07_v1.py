import re

#Works out whether string has numbers and seperates string into amount and item.

test_strings = [
  "Popcorn",
  "2 pc",
  "1.5OJ",
  "4OJ"
]

for item in test_strings:
  
  #regular expression to find if item starts with a number
  number_regex = "^[1-9]"
  
  #if item has a number, seperate it into 2 (number / item)
  if re.match(number_regex, item):
    amount = int(item[0])
    desired_snack = item[1:]
  #if item doesn't have a number, set number as 1
  else:
    amount = 1
    desired_snack = item
    
  #remove white space around snack
  desired_snack = desired_snack.strip()
  
  #Print Order
  print("Amount:", amount)
  print("Snack:", desired_snack)
  print("Length of snack:", len(desired_snack), " \n")