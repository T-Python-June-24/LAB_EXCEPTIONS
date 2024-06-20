import os

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
 
def celsius_to_fahrenheit(celsius:float)->float:
    fahrenheit = (celsius * 9/5) + 32
    
    return f"\n  \033[32m convert {celsius} from celsius to fahrenheit =  {round(fahrenheit,2)} "

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9

    return f"\n  \033[32m convert {fahrenheit} from fahrenheit to celsius =  {round(celsius,2)} "

def main():
        
    user_input = input('\nPlease enter a temperature and its unit (e.g., "25 C" or "77 F") : ')

    temprature = user_input.split() 
    
    if not temprature[0].isnumeric():
        raise ValueError(" You enterd an invalid number of temperature that contain characters or symbols !")    

    elif not (len(temprature) > 2 or len(temprature) < 2) :
        if temprature[1].upper() == "C":
            print(celsius_to_fahrenheit(float(temprature[0])))
        elif temprature[1].upper() == "F":
            print(fahrenheit_to_celsius(float(temprature[0])))
        else: 
            raise TypeError(" Temperature unit must be Fahrenheit or Celsius only !")

    else :
        raise ValueError(" You enterd invalid temperature ! ")

clear_terminal()
while True:
    print('''
\033[37m \033[45m  Welcome to Temperature Converter app 🌡️ \033[0m \033[35m
''')
    try:
        main()
    except TypeError as e : 
        print("\n \033[31m  Error: ",e,"\033[0m")
        input("\n \033[35m  Press Enter to continue...")
        clear_terminal()
    except ValueError as e :
        print("\n \033[31m  Error: ",e,"\033[0m")
        input("\n \033[35m  Press Enter to continue...")
        clear_terminal()
    else:
        print('''
\n \033[33m Thank you for using Temperature Converter.. Goodbye 👋 \n
''')
        break



