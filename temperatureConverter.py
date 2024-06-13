def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    x = input("Enter a temperature and its unit (e.g., 25 C or 77 F):")
    x = x.split(" ")
    temp = float(x[0])
    unit = x[1]

    if unit.upper() == "F":
        celsius = fahrenheit_to_celsius(temp)
        celsius = round(celsius,2)
        print(f"Temperature in Celsius: {celsius} C")
    elif unit.upper() == "C":
        fahrenheit = celsius_to_fahrenheit(temp)
        fahrenheit = round(fahrenheit ,2)
        print(f"Temperature in fahrenheit: {fahrenheit} F")
    else:
        raise Exception("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit")


#main program
while True:
    try:
        main()
    except ValueError:
        print("Invalid input. Please enter temperature in correct form (e.g. 25 C or 77 F)")
    except Exception as e:
        print(e)
