#Initalize Snack Lists...
import pandas

test_names = ['a', 'b', 'c', 'd', 'e']
#test_names = [1]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
names = test_names
# names = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data Frame Dictionary
movie_data_dict = {
  'Name': names,
  'Popcorn': popcorn,
  'M&Ms': mms,
  'Pita Chips': pita_chips,
  'Water': water,
  'Orange Juice': orange_juice
}

test_data = [
  [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
  [[]],
  [[1, 'Water']],
  [[1, 'Popcorn'], [1, 'Orange Juice']],
  [[1, 'Pita Chips'], [1, 'Water'], [3, 'Orange Juice']]
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
    if len(item) > 0:
      to_find = (item[1])
      amount = (item[0])
      add_list = movie_data_dict[to_find]
      add_list[-1] = amount

print("Snack Tally:")
print("Popcorn: ", snack_lists[0])
print("M&Ms: ", snack_lists[1])
print("Pita Chips: ", snack_lists[2])
print("Water: ", snack_lists[3])
print("Orange Juice: ", snack_lists[4], " \n")

#print
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)