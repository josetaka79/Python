motorcycles=['honda', 'yamaha', 'suzuki', 'kwid']
print(motorcycles)

popped_motorcycle= motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f'The last motorcycle i owned was a {last_owned.title()}')

first_owned =motorcycles.pop(0)
print (f"The first motorcycle i owned was a {first_owned.title()}")