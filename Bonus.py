
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

while True: 
    try:
        user_input = input("Enter a temperature and its unit separated by a space (e.g., '25 C' or '77 F'): ")
        s=user_input.split(" ")
        unit=s[1]
        temp=s[0]

        if unit != 'F' and unit != 'C':
            raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        if not float(temp):
            raise ValueError("The temperature must be a digit only")

    except TypeError as e:
        print(e)

    except ValueError as e:
        print(e)

    else: 
        if unit == 'F':
            temp = fahrenheit_to_celsius(float(temp))
            r=round(temp,2)
            print(f"Temperature in Celsius: {r} C")
            break
        elif unit == 'C':
            temp = celsius_to_fahrenheit(float(temp))
            r=round(temp,2)
            print(f"Temperature in Fahrenheit: {r} F")
            break