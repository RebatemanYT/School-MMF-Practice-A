#Initalize Snack Lists...
import pandas

test_names = ['a', 'b', 'c', 'd', 'e', 'f']
#test_names = [1]
#all_ages = [15, 104, 55, 60, 100, 25]
all_tickets = [7.5, 6.5, 10.5, 10.5, 6.5, 10.5]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
names = test_names
# names = []
# ages = all_ages
# ages = []
tickets = all_tickets
tickets = []
ticket_prices = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data Frame Dictionary
movie_data_dict = {
  'Name': names,
#  'Age': ages,
  'Ticket Value': tickets,
  'Popcorn': popcorn,
  'M&Ms': mms,
  'Pita Chips': pita_chips,
  'Water': water,
  'Orange Juice': orange_juice
}

price_dict = {
  'Popcorn': 2.5,
  'M&Ms': 2,
  'Pita Chips': 4.5,
  'Water': 3,
  'Orange Juice': 3.25
}

test_data = [
  [[2, 'Popcorn'], [1, 'M&Ms']],
  [[]],
  [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice'], [1, 'Water'], [1, 'M&Ms']],
  [[2, 'Popcorn'], [1, 'Pita Chips'], [4, 'Orange Juice']],
  [[1, 'Popcorn'], [1, 'M&Ms'], [1, 'Water']],
  [[4, 'Popcorn'], [4, 'Pita Chips'], [4, 'Water'], [4, 'Orange Juice'], [4, 'M&Ms']]
]

count = 0
for client in test_data:
  #Assume no snacks have been brought
  for item in snack_lists:
    item.append(0)

  #print(snack_lists)
  snack_order = test_data[count]
  tickets = all_tickets
  count += 1
  
  for item in snack_order:
    if len(item) > 0:
      to_find = (item[1])
      amount = (item[0])
      add_list = movie_data_dict[to_find]
      add_list[-1] = amount

#print
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame['Sub Total'] = \
  movie_frame['Ticket'] + \
  movie_frame['Popcorn']*price_dict['Popcorn'] + \
  movie_frame['Water']*price_dict['Water'] + \
  movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
  movie_frame['M&Ms']*price_dict['M&Ms'] + \
  movie_frame['Orange Juice']*price_dict['Orange Juice']
print(movie_frame)