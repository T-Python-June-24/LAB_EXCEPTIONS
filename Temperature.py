import re

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def mainFunction():
    while True:
        try:
            temperature = input("Please enter temperature degree and its unit to convert (e.g., '57 C'): ")
            parts = temperature.split()
            
            # Check if there are exactly two parts (number and unit)
            if len(parts) != 2:
                raise ValueError("Invalid temperature format")
            
            temperature_value = float(parts[0])
            
            temperature_unit = parts[1].upper()
            if temperature_unit not in ['C', 'F']:
                raise ValueError("Invalid temperature unit")
            
            
            if temperature_unit == 'C':
                result = celsius_to_fahrenheit(temperature_value)
                print(f"{temperature_value} C is equal to {result:.2f} F")
            else:
                result = fahrenheit_to_celsius(temperature_value)
                print(f"{temperature_value} F is equal to {result:.2f} C")
            
            break  
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

mainFunction()