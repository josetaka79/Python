# Class definition
# -------------------------
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant with name and cuisine type"""
        self.restaurant_name = restaurant_name   # attribute 1
        self.cuisine_type = cuisine_type         # attribute 2

    def describe_restaurant(self):
        """Print the restaurant's details"""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message that the restaurant is open"""
        print(f"{self.restaurant_name} is now open! 🍽️")


# -------------------------
# Create an instance (object)
# -------------------------
restaurant = Restaurant("FanickJ's Kitchen", "African Food")

# -------------------------
# Access attributes directly
# -------------------------
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# -------------------------
# Call the methods
# -------------------------
restaurant.describe_restaurant()
restaurant.open_restaurant()