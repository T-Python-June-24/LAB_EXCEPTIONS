# Temperature Converter

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)


def main():
    try:   
        user_choice = input("Enter the temperature (number) and the unit (C/F) seperated by space: like 23 C or 86 F: ").lower().split()
        temperature, unit = user_choice
        temperature = float(temperature)
        if unit.upper() == "C":
            print(f"{temperature} Celsius is {celsius_to_fahrenheit(temperature)} Fahrenheit")
        elif unit.upper() == "F":
            print(f"{temperature} Fahrenheit is {fahrenheit_to_celsius(temperature)} Celsius")
            
    except ValueError:
        print("Please enter a valid temperature and unit. Like 23 C or 86 F.")
    
    except TypeError:
        print("Please enter a valid temperature and unit. Like 23 C or 86 F.")
    
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Thank you for using the temperature converter!")

main()