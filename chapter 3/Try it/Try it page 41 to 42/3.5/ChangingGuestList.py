Guest=["Ncha", "Khan", "Fru", "Anucha", "Desmond"]
#print(Guest[2])
#print(Guest[3])

del Guest[2]
del Guest[3]

Guest.insert(2, "Edith")
print(Guest)
Guest.insert(3, "Nchang")
print(Guest)

Guest=["Ncha","Khan", "Edith", "Nchang", "Desmond"]
print(Guest)

for guest in Guest:
  message = f" You are invited for a dinner tonight, {guest}."
  print(message)

