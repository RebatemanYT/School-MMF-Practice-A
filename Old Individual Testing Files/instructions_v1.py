yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

#String Check
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name of the snack
        if choice in var_list:

            # Get full name of snack and put it in title case so it looks nice when outputted
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
        print("Please enter a valid option")
        print()
        return "invalid choice"

#Function to show instructions if needed.
def instructions(options):
  #loop
  show_help = "invalid choice"
  while show_help == "invalid choice":
    #ask question
    show_help = input("Would you like to see the instructions? \n").lower()
    string_check(show_help, options)
    
    #bc of having issues w/ the loop, had to do this to make sure the loop would loop.
    if show_help == "yes" or show_help == "y" or show_help == "no" or show_help == "n":
      show_help = show_help
    else:
      show_help = "invalid choice"
  if show_help == "yes" or show_help == "y":
    #instructions
    print()
    print("INSTRUCTIONS:")
    print()
    print("1st step: Input name. \n2nd step: Input your age. \n3rd step: Input which snacks you want. In case of change in snacks, the snacks will always be listed. Note that there's a 4 per person per snack type limit. \n4th step: Input if you want to pay with card or credit. \n5th step: Done.")
  return ""

#Main Part


instructions(yes_no)
print()
print("Program launching...")
from MMF_base_00_v8 import *