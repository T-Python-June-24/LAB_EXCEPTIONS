class InvalidUnitError(TypeError):
    """Raised when the input unit is invalid"""
    pass

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            temp_str, unit = user_input.split()
            temperature = float(temp_str)
            
            if unit.upper() == 'C':
                converted_temp = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {converted_temp:.2f} F")
            elif unit.upper() == 'F':
                converted_temp = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {converted_temp:.2f} C")
            else:
                raise InvalidUnitError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            
        except ValueError as e:
            print(f"A ValueError occurred: {e}")
            print("Invalid temperature value. Please enter a valid number.")
        except InvalidUnitError as e:
            print(f"An InvalidUnitError occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

main()
