"""
EXERCISE 1.3: Temperature Converter - SOLUTION
"""

# Ask for temperature in Celsius
celsius = input("Temperature in Celsius: ")
celsius = float(celsius)

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Convert to Kelvin
kelvin = celsius + 273.15

# Display the results
print(f"{celsius}°C = {fahrenheit}°F = {kelvin}K")
