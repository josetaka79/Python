# city_functions.py

#def city_country(city, country):
    #"""Return a single string of the form 'City, Country'."""
    #formatted_location = f"{city.title()}, {country.title()}"
    #return formatted_location


# Example usage (this line will display the result when you run the file directly)
#if __name__ == "__main__":
    #print(city_country('santiago', 'chile'))
    
   # city_functions.py

# city_functions.py
#def city_country(city, country, population):
    #"""Return a string formatted as 'City, Country - population xxx'."""
    #return f"{city.title()}, {country.title()} - population {population}"
    
    # city_functions.py

def city_country(city, country, population=None):
    """Return a neatly formatted city and country, with optional population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    
  



