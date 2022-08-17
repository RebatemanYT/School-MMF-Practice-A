# Function goes here
import re
#regular expression to find if item starts with a number - some need 0, some don't.
number_regex_0_9 = "^[0-9]"

is_valid = ""
def string_check(choice, options, error):

    for var_list in options:

        # if the snack is in one of the lists, return the full name of the snack
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            hasnum = "no"
            continue

        # if the chosen option is not valid, set is_valid to no
        else:
          if re.match(number_regex_0_9, choice):
            chosen_num = int(choice[0])
            chosen_var = var_list[0].title()
            is_valid = "yes"
            hasnum = "yes"
            continue
          else:
            is_valid = "no"
            continue

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
      if hasnum == "yes":
        chosen = ""
        chosen += "", chosen_num, chosen_var, ""
        print(chosen)
        return chosen
      else:
        print(chosen)
        return chosen
    else:
      return error


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
number_regex_1_9 = "^[1-9]"
number_regex_1_5 = "^[1-5]"

check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack = string_check(want_snack, yes_no, "Error: \n" "Invalid Choice")
  
  if re.match(number_regex_0_9, want_snack):
    want_snack = want_snack[1:]
  #If want_snack is valid and a Yes input, continue.
  if want_snack == "yes" or want_snack == "ye" or want_snack == "ys" or want_snack == "es" or want_snack == "y" or want_snack == "e" or want_snack == "s":
    loop_count = 0
    loop_max = 6
    snack_list = ""
    loop_exit = 0
    snack_choice = ""
    desired_snack = ""
    # 6 loops OR exit code ("Done") to end
    while loop_exit == 0:
      while loop_max - loop_count != 0:

      # ask user for desired snack and put it in lowercase
        print("You currently have", loop_max - loop_count, "more input(s) for snacks. Your current options: \n" "a. Popcorn \n" "b. M&M's \n" "c. Pita Chips \n" "d. Water \n" "e. Done (ends loop) \n")
        desired_snack = input("Snack: ").lower()
        snack_choice_error = "Error: \n" "Either you inputed an invalid snack OR you inputted that you want too much or too little of a snack (5 per person max)."

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks, snack_choice_error)
        if snack_choice == "invalid choice":
          print(snack_choice_error)
          continue
        elif snack_choice in valid_snacks:
          #if item doesn't have a number, set number as 1
          amount = 1
          desired_snack = snack_choice
          continue
        elif re.match(number_regex_1_9, snack_choice[0]):
          if re.match(number_regex_1_5, snack_choice[0]):
            amount = int(snack_choice[0])
            desired_snack = snack_choice[1:]
            continue
          else:
            print(snack_choice_error)
            continue

          
        #remove white space around snack
        desired_snack = desired_snack.strip()
          
        if desired_snack == "done" or "xxx" or "e":
          desired_snack = "done"
          loop_count = loop_max
          continue
        elif snack_list == "":
          snack_list = loop_count, "-", amount, desired_snack, " \n"
          continue
        else:
          snack_list += loop_count, "-", amount, desired_snack, " \n"
          continue
        loop_count = loop_count + 1
          #Print Order
        print("Amount:", amount)
        print("Snack:", desired_snack)
        print("Length of snack:", len(desired_snack), " \n")

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
  print("Snack List:")

  if loop_exit == 1:
    print("None \n")
  else:
    print(snack_list)
  
print("Test - Exited Loop")