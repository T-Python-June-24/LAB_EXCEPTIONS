
def celsius_to_fahrenheit(celsius:float)->float:
    fahrenheit = (celsius * 9/5) + 32
    
    return f" {"-"*100}\n   | convert from celsius to fahrenheit =  {round(fahrenheit,2)} | "

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9

    return f" {"-"*100}\n   | convert from fahrenheit to celsius =  {round(celsius,2)} | "

def main():
        
    user_input = input('\nPlease enter a temperature and its unit (e.g., "25 C" or "77 F") \n')

    temprature = user_input.split() 


    
    if not temprature[0].isnumeric():
        raise ValueError("\n   ( You enterd an invalid number of temperature that contain characters or symbols ! ) \n ")    

    elif not (len(temprature) > 2 or len(temprature) < 2) :
        if temprature[1].upper() == "C":
            print(celsius_to_fahrenheit(float(temprature[0])))
        elif temprature[1].upper() == "F":
            print(fahrenheit_to_celsius(float(temprature[0])))
        else: 
            raise TypeError("\n ( Temperature unit must be Fahrenheit or Celsius only ! )\n ")

    else :
        raise ValueError("\n  ( You enterd invalid temperature ! ) \n ")

print(f"{"-"*100}\n  | Welcome to Temperature Converter app |\n {"-"*100}")
while True:
    try:
        main()
    except TypeError as e : 
        print(e)
    except ValueError as e :
        print(e)
    else:
        print(f"\n   Thank you for using Temperature Converter.. Goodbye \n {"-"*100}")
        break



