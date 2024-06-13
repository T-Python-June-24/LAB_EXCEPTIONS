def addition (x,y):
    ''' this function is for adding to positive numbers'''
    x = 10
    y = 20
    print("Addition:" , x + b)
    print("The operation is successful")

try:
    addition(10,1)
except NameError as e:
    print("There is variable not defined")
    print(e)