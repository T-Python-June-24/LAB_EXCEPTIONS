def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)


def main():
    try:   
        user_choice = input("Enter temperature (number) and the unit (C/F) seperated : like 23 C or 86 F: ").split()
        temperature, unit = user_choice
        temperature = float(temperature)
        if unit == "C":
            print(f"{temperature} Celsius is {celsius_to_fahrenheit(temperature)} Fahrenheit")
        elif unit== "F":
            print(f"{temperature} Fahrenheit is {fahrenheit_to_celsius(temperature)} Celsius")

    except ValueError:
        print("Please enter temperature and unit. Like 23 C or 86 F.")

    except TypeError:
        print("Please enter temperature and unit. Like 23 C or 86 F.")

    except Exception as e:
        print("error :", e)
    else:
        print("successfully!")

main()