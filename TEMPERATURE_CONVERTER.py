def celsius_to_fahrenheit(celsius:str) -> str:
    return str(round((float(celsius) * 9 / 5) + 32, 2))

def fahrenheit_to_celsius(fahrenheit:str) -> str:
    return str(round((float(fahrenheit) - 32 ) * 5 / 9, 2))

def validate_unit(unit:str):
    if unit == "C" or unit == "F":
        return
    raise TypeError

def validate_number(number:str):
    strings = number.split(".")
    for string in strings:
        if not string.isdigit():
            raise ValueError
    return
     
def main():
    while True:
        print()
        temperature:str = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        try:
            number, unit = temperature.split()
        except ValueError:
            print('Your input should look like: "25 F"')
            continue
        else:
            try:
                validate_number(number)
                validate_unit(unit)
            except ValueError:
                print("Invalid temperature value. Try again")
                continue
            except TypeError:
                print("Invalid unit. Try again.")
                continue
            else:
                if unit.upper() == "C":
                    print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(number)} F")
                    break
                elif unit.upper() == "F":
                    print(f"Temperature in Celcius: {fahrenheit_to_celsius(number)} C")
                    break

main()
    