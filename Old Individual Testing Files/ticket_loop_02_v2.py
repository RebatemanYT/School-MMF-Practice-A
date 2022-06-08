#Start of loop

#initalise loop so that it runs at least once
name = ""
count = 0
MAX_TICKET = 5

while name != "xxx" and count < MAX_TICKET:
  print("You have {} seats "
       "left".format(MAX_TICKET - count))

  #Get details
  name = input("Name: ")
  count += 1
  if name != "xxx":
    print("Ticket sold. \n")

if count == MAX_TICKET:
  print("You have ran out of available tickets.")
else:
  print("You have sold {} tickets  \n"
       "You have {} tickets left."
       .format(count, MAX_TICKET - count))