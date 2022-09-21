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

inst_text = "1st step: Input name. 2nd step: Input your age. 3rd step: Input which snacks you want. In case of change in snacks, the snacks will always be listed before you start checking. Note that there's a 4 per person per snack type limit. 4th step: Input if you want to pay with card or credit. 5th step: Done."

def instructions(options):
  show_help = "invalid choice"
  while show_help == "invalid choice":
    show_help = input("Would you like to see the instructions?").lower()
    string_check(show_help, options)
  if show_help == "yes" or show_help == "y":
    print()
    print("INSTRUCTIONS:")
    print()
    print(inst_text)
  return ""

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

#Main Part


instructions(yes_no)
print()
print("Program launching...")
from MMF_base_00_v8 import *