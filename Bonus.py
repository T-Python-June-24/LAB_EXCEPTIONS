"""
    The main function that handles the user input and conversion of temperature units.

    This function prompts the user to enter a temperature and its unit (either Celsius or Fahrenheit),
    then converts the temperature to the other unit and prints the result.

    Raises:
        TypeError: If the user enters an invalid unit (not 'C' or 'F').
        ValueError: If the user enters a non-numeric value for the temperature.
"""

class TypeError(Exception):
   
   """ If the user enters an invalid unit (not 'C' or 'F') """

def fahrenheit_to_celsius(fahrenheit):
   celsius = round(((fahrenheit - 32) * 5/9),2)
   return celsius
def celsius_to_fahrenheit(celsius):
  fahrenheit = round(((celsius * 9/5) + 32),2)
  return fahrenheit
  

def main():
  
    
    temperature_and_unit = input("Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\"): ")

    input_splited=temperature_and_unit.split(" ")
     
    if input_splited[1].upper()!="F" :
        if input_splited[1].upper()!="C" :
         raise TypeError(" Please enter a vaild Type  eg( C ,F) ")
    
    if input_splited[1].upper()=="F":
     fahrenheit=input_splited[0]
     Fahrenheit=float(fahrenheit)
     celsius=fahrenheit_to_celsius(Fahrenheit)
     print(f"Temperature in Celsius: {celsius} C")

    if input_splited[1].upper()=="C":
     celsius=input_splited[0]
     Celsius=float(celsius)
     fahrenheit=celsius_to_fahrenheit(Celsius)
     print(f"Temperature in fahrenheit: {fahrenheit} F")


while True:
    try:
        main()
    except ValueError as e :
       print(f"{e}  Please enter a number  ")
       
    except TypeError as e :
       print(e)
    except Exception as e :
       print(e) 


