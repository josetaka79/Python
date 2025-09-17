# person dictionary
person = {
    'name': 'Alice',
    'age': 30,
}
# Looping through all key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
    
    # Looping through all keys
    for key in person.keys():
        print(key)
        
      # Favorite colors dictionary
    favorite_colors = {
          'Alice': 'blue',
          'Bob': 'green',
          'Charlie' : 'red',
      }  
    
    # Looping through keys in a particular order (alphabetically)
    for name in sorted(favorite_colors.keys()):
        print(name)
        
        # Looping through all values in the dictionary
        for color in favorite_colors.values():
            print(color)
            
            # list of dictionaries, each representing a car's details
            cars = [
                {'make': 'Toyota', 'model': 'Corolla', 'color': 'blue'},
                {'make': 'Honda', 'model': 'Civic', 'color': 'red'},
                {'make':'Ford', 'model': 'Mustang', 'color': 'black'}
                
            ]
            
            #Loop through the list of dictionaries and print each car's details
            for car in cars:
                print(f"Car: {car['make']} {car['model']}, color:{car['color']}")
                
                # Dictionary containing a list of car colors
                garage = {
                    'colors': ['blue', 'red', 'black', 'white', 'green'],
                    'location': 'San francisco'
                }
                
                # Accessing and printing the list of car colors in the dictionary
                print(f"Garage location: {garage['location']}")
                print("Available Colors for cars:")
                for color in garage['colors']:
                    print(f"- {color}")
                    
                    
                    # Define the dictionary
                    users = {
                        'jdoe':{
                            'first_name': 'John',
                            'last_name': 'Doe',
                            'location': 'New York'
                        },
                        'jsmith': {
                        'first_name': 'Jane',
                        'last_name': 'Smith',
                        'location': 'Los Angeles'
                            
                        }
                    }
                    # Looping through the outer dictionary to get user data
                    for username, user_info in users.items():
                        print(f"\nusername: {username}")
                        
                        #accessing and printing values from the inner dictionary
                        full_name = f"{user_info['first_name']} {user_info['last_name']}"
                        location = user_info['location']
                        
                        print(f"Full Name: {full_name}")
                        print(f"Location: {location}")