#Start of loop

#initalise loop so that it runs at least once
name = ""
count = 0
MAX_TICKET = 2

while name != "xxx" and count < MAX_TICKET:
  if count == MAX_TICKET - 1:
    #When 1 seat is left, don't say seats, say seat.
    print("You have {} seat "
       "left".format(MAX_TICKET - count))
  else:
    #In every other case, say seats.
    print("You have {} seats "
       "left".format(MAX_TICKET - count))

  #Get details
  name = input("Name: ")
  if name != "xxx":
    #Excluding the exit code from counting towards sold tickets.
    count += 1
    print("Ticket sold. \n")

if count == MAX_TICKET:
  #Lack of tickets = no more code running.
  print("You have ran out of available tickets.")
#Rest are correcting grammatical issues. 

elif MAX_TICKET - count == MAX_TICKET - 1 & MAX_TICKET - count == 1:
  #1 ticket sold and 1 ticket left.
  print("You have sold {} ticket  \n"
       "You have {} ticket left."
       .format(count, MAX_TICKET - count))

elif MAX_TICKET - count == MAX_TICKET - 1:
  #1 ticket sold and multiple tickets left.
  print("You have sold {} ticket  \n"
       "You have {} tickets left."
       .format(count, MAX_TICKET - count))

elif MAX_TICKET - count == 1:
  #Multiple tickets sold and 1 ticket left.
  print("You have sold {} tickets  \n"
       "You have {} ticket left."
       .format(count, MAX_TICKET - count))

else:
  #Multiple tickets sold and multiple tickets left.
  print("You have sold {} tickets  \n"
       "You have {} tickets left."
       .format(count, MAX_TICKET - count))