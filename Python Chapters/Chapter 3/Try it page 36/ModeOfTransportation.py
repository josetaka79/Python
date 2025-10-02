# Create a list of car brands
cars = ["mazda", "toyota", "ford", "kwid"]

# Loop through each car in the list
for car in cars:
    # Create a message that includes the car name in title case
    # .title() capitalizes the first letter of each word
    message = f"I admire {car.title()}."
    
    # Print the message
    print(message)