# Assign a color to the alien
alien_color = "green"  # The alien's color is currently green

# Use an if-elif-else chain to assign points based on the alien's color
if alien_color == "green":  # Check if the alien is green
    # This block executes if the alien is green
    print("Player earned 5 points!")  # Player earns 5 points
elif alien_color == "yellow":  # Check if the alien is yellow
    # This block executes if the alien is yellow
    print("Player earned 10 points!")  # Player earns 10 points
else:  # If the alien is neither green nor yellow
    # This block executes for any other color (e.g., red)
    print("Player earned 15 points!")  # Player earns 15 points
