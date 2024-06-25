def C2F (celsius):
    F1 = round(((celsius * 9/5) + 32),2)
    print(F1)

C2F(int(input("insert a Celsius temperature to change to Fahreheit: ")))

def F2C (fahrenheit):
    C1 = round(((fahrenheit - 32) * 5/9),2)
    print(C1)

F2C(int(input("insert a Fahreheit temperature to change to Celsius: ")))