#Initalize Snack Lists...

test_names = ['1', '2', '3']
#test_names = [1]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
names = test_names
# names = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
  'Popcorn': popcorn,
  'M&Ms': mms,
  'Pita Chips': pita_chips,
  'Water': water,
  'Orange Juice': orange_juice
}

test_data = [
  [[1, 'Water'], [1, 'Pita Chips'], [1, 'M&Ms']],
  [[1, 'Water'], [1, 'Water'], [1, 'Orange Juice'], [2, 'M&Ms']],
  [[1, 'Popcorn']]
]

count = 0
for client in test_data:
  #Assume no snacks have been brought
  for item in snack_lists:
    item.append(0)

  #print(snack_lists)
  snack_order = test_data[count]
  count += 1
  
  for item in snack_order:
    to_find = (item[1])
    amount = (item[0])
    add_list = snack_menu_dict[to_find]
    add_list[-1] = amount

print(snack_lists)