# Define the function with a default country
def describe_city(city, country="South Africa"):
    print(f"{city} is in {country}.")

# Call the function for three different cities

# City in the default country (Iceland)
describe_city("Johannesburg")

# Another city in the default country
describe_city("Durban")

# City not in the default country
describe_city("Douala", country="Cameroon")