# city_functions.py
# This module defines a function that formats a city, country, and optional population.

def city_country(city, country, population=None):
    """Return a string formatted as 'City, Country' or
    'City, Country - population xxx' if population is provided."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    
