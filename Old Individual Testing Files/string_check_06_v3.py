# Function goes here
is_valid = ""
def string_check(choice, options, error):

    for var_list in options:

        # if the snack is in one of the lists, return the full name of the snack
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
      return "invalid choice"


# Valid snacks holds list of all snacks. Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e), and possible abbreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],    # first item is M&M's for inclusion in output
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["done", "xxx", "e"]
]
#Yes or no.
yes_no = [
    ["yes", "ye", "ys", "es", "y", "e", "s"],
    ["no", "n", "o", "x"],
    ["error"]
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack = string_check(want_snack, yes_no, "Error: \n"
                               "Invalid Choice")
  
  #If want_snack is valid and a Yes input, continue.
  if want_snack == "yes" or want_snack == "ye" or want_snack == "ys" or want_snack == "es" or want_snack == "y" or want_snack == "e" or want_snack == "s":
    loop_count = 0
    loop_max = 6
    snack_list = ""
    loop_exit = 0
    snack_choice = ""
    # 6 loops OR exit code ("Done") to end
    while loop_max - loop_count != 0 or loop_exit == 0:
      while snack_choice != "Done":

      # ask user for desired snack and put it in lowercase
        print("You currently have", loop_max - loop_count, "more input(s) for snacks. Your current options: \n" "a. Popcorn \n" "b. M&M's \n" "c. Pita Chips \n" "d. Water \n" "e. Done (ends loop) \n")
        desired_snack = input("Snack: ").lower()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks, "Error: \n" "Either you inputed an invalid snack OR you inputted that you want too much of a snack (5 per person max).")
        if snack_choice == "Done":
          continue
        elif snack_choice == "invalid choice":
          print("Error: Invalid Choice")
        else:
          print("Snack Choice: ", snack_choice)
          if snack_list == "":
            snack_list = snack_choice
          else:
            snack_list += snack_choice
          snack_list += " \n"
          loop_count = loop_count + 1
      print("Seems like you have finished. \n" "Snack List:")
      if loop_count == 0:
        loop_exit = 1
        loop_count = loop_max
        continue
      else:
        loop_count = loop_max
        loop_exit = 2
        continue
  elif want_snack == "no" or want_snack == "n" or want_snack == "o" or want_snack == "x":
    #Valid + a no input for want_snack = this.
    print("No snacks. Got it.")
    continue
  else:
    #Every other option leads to error and loop.
    want_snack = "error"
    print("Error: \n" "Not a valid input.")
    continue

  if loop_exit == 1:
    print("None \n")
  else:
    print(snack_list)
  
print("Test - Exited Loop")