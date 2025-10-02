# Define the function to store car information
def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with required info and additional keyword arguments
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to check all information
print("\n--- Car Information ---")
for key, value in car.items():
    print(f"{key}: {value}")