# Define the User class
class User:
    def __init__(self, first_name, last_name, **user_info):
        """
        Initialize a user with first and last name, plus other optional attributes.
        Parameters:
            first_name (str): User's first name
            last_name (str): User's last name
            user_info (dict): Other optional user attributes like email, age, location
        """
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info  # Store additional attributes in a dictionary

    def describe_user(self):
        """
        Print a summary of the user's information.
        """
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.user_info.items():
            print(f"{key.capitalize()}: {value}")

    def greet_user(self):
        """
        Print a personalized greeting to the user.
        """
        print(f"Hello {self.first_name} {self.last_name}! Welcome back!\n")

# Create several user instances with different information
user1 = User("Alice", "Smith", email="alice@example.com", age=28, location="New York")
user2 = User("Bob", "Johnson", email="bob@example.com", age=35, location="London")
user3 = User("Charlie", "Brown", email="charlie@example.com", age=22, location="Sydney")

# Call describe_user() and greet_user() for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()