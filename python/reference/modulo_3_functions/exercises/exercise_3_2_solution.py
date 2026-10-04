"""
EXERCISE 3.2: Temperature Converter - SOLUTION
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    try:
        return (float(celsius) * 9/5) + 32
    except (ValueError, TypeError):
        print("Invalid temperature value!")
        return None

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    try:
        return (float(fahrenheit) - 32) * 5/9
    except (ValueError, TypeError):
        print("Invalid temperature value!")
        return None

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    try:
        return float(celsius) + 273.15
    except (ValueError, TypeError):
        print("Invalid temperature value!")
        return None

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    try:
        return float(kelvin) - 273.15
    except (ValueError, TypeError):
        print("Invalid temperature value!")
        return None


# Test the functions
print("=== Temperature Converter Tests ===")
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")
print(f"25°C = {celsius_to_kelvin(25):.2f}K")
print(f"298.15K = {kelvin_to_celsius(298.15):.1f}°C")
print()

# BONUS: Universal converter
def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature between any units.
    
    Args:
        value (float): Temperature value
        from_unit (str): 'C', 'F', or 'K'
        to_unit (str): 'C', 'F', or 'K'
    
    Returns:
        float: Converted temperature
    """
    try:
        value = float(value)
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        # If same unit, return value
        if from_unit == to_unit:
            return value
        
        # Convert to Celsius first
        if from_unit == 'F':
            celsius = (value - 32) * 5/9
        elif from_unit == 'K':
            celsius = value - 273.15
        else:  # Already Celsius
            celsius = value
        
        # Convert from Celsius to target unit
        if to_unit == 'F':
            return (celsius * 9/5) + 32
        elif to_unit == 'K':
            return celsius + 273.15
        else:  # Stay Celsius
            return celsius
    
    except (ValueError, TypeError):
        print("Invalid input!")
        return None

print("=== BONUS: Universal Converter ===")
print(f"100°C in Fahrenheit: {convert_temperature(100, 'C', 'F'):.1f}°F")
print(f"32°F in Kelvin: {convert_temperature(32, 'F', 'K'):.2f}K")
print(f"300K in Celsius: {convert_temperature(300, 'K', 'C'):.2f}°C")
