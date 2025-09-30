#1. Define a class called Dog:
class Dog:
    """A simple attempt to model a dog."""
    
    # The _init_ method is the constructor that gets called when we create an instance of Dog
    def _init_(self, name, age):
        """Initialize name and age attributes for the dog."""
        self.name = name  # Assign the given 'name' to the instance's 'name' attribute
        self.age = age  # assign the given 'age' to the instance's 'age' attribute
        
        # method that shows a dog sitting
        def sit(self):
            print(f"{self.name} is now sitting.")
            
            # Method that shows a dog rolling over
            def roll_over(self):
                print(f"{self.name} rolled over!")
                
                #2. Creating an instance:
                my_dog = Dog('Willie', 6)
                print(f"My dog's name is {my_dog.name}.")