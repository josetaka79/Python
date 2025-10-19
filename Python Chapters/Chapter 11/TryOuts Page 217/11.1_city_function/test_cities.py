

# test_cities.py
from City_functions import city_country

def test_city_country():
    """Test the function without population (will fail)."""
    result = city_country('santiago', 'chile')  # no population argument
    assert result == 'Santiago, Chile'

def test_city_country_population():
   # """Test the function with population (will pass)."""
    """Test city_country() with a population value."""
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile - population 5000000'