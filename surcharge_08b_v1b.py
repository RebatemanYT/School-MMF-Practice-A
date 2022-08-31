import re
import pandas

#Reminder: Response is in capitals
def string_check(choice, options):

    is_valid = ""
    chosen = ""

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
        print("Please enter a valid option \n")
        return "invalid choice"
#string no longer checking


# Main Routine
pay_method = [
  ["cash", "ca", "a"],
  ["credit", "cr", "ce", "r", "card", "credit card"]
]

#Loop until exit code
name = ""
while name != "xxx":
  name = input("Name: ")
  if name == "xxx":
    break
  #Asking for payment method
  how_pay = "invalid choice"
  while how_pay == "invalid choice":
    how_pay = input("Please choose a payment method (cash or credit). \nNote that to pay by credit, there's a surcharge of 5%.").lower()
    how_pay = string_check(how_pay, pay_method)

  # Ask for subtotal (testing)
  subtotal = float(input("Sub Total? $"))
  
  if how_pay == "Credit":
    surcharge = 0.05 * subtotal
  else:
    surcharge = 0
  
  total = subtotal + surcharge
  
  print("| Name: {} |".format(name), "Subtotal: {:.2f} |".format(subtotal), "Surcharge: {:.2f} |".format(surcharge), "Total: {:.2f}".format(total))