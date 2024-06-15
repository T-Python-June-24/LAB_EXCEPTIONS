def celsius_to_fahrenheit() -> float:
    while True :
        tempInput = input("Please Enter celsius temperature:")
        try:
            temp, unit = tempInput.split(" ")
            temp = float(temp)

            if unit.upper() != "C" :
                raise TypeError
            fahrenheit = (temp * 9/5) + 32
            return print(f"\n The temperature {tempInput} has been converted successfully to  {fahrenheit} F \n")

        except ValueError:
            print("Please Enter valid temperature value")
        except TypeError as e:
            print(f"{unit} is invalid, Please Enter valid temperature uint")

def fahrenheit_to_celsius() -> float:
    while True :
        tempInput = input("Please Enter fahrenheit temperature:")
        try:
            temp, unit = tempInput.split(" ")
            fahrenheit = float(temp)

            if unit.upper() != "F" :
                raise TypeError
            celsius = (fahrenheit - 32) * 5/9
            return print(f"\n The temperature {tempInput} has been converted successfully to  {celsius} C \n")
        
        except ValueError:
            print("Please Enter valid temperature value")
        except TypeError as e:
            print(f"{unit} is invalid, Please Enter valid temperature uint")
    

def main ():

    while True:
        print("\nTemperature Converter Please choose the Temperature unit:\n")
        print("1. Convert from Celsius(C) to Fahrenheit(F)")
        print("2. Convert from Fahrenheit(F) to Celsius(C)")
        print("3. Exit")
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            celsius_to_fahrenheit()
        elif choice == "2":
            fahrenheit_to_celsius()
        elif choice == "3":
            print("Exiting Program ...")
            break
        else:
            raise Exception("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()