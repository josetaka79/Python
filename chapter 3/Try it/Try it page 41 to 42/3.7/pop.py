Guest=["Ncha", "Khan", "Fru", "Anucha", "Desmond", "Juliet"]
print(Guest)
    
for guest in Guest:
     #message=(f"Yor are cordially invited for a dinner tonight, {guest}")
     #print(message)
    
    # message=(f" I can only invite 2 people for dinner{guest}")
     #print(message)
         
     popped_guest=Guest.pop(0)
     #print(Guest)
    # print(popped_guest)
     message=(f"I am sorry, I can't invite you to dinner, {popped_guest.title()}")
     print(message)