
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
#After printing the raised error is (NameError: name 'b' is not defined)

try:
    additoin(10, 20)
except NameError as e:
    print("Variable error in  the method")
else:
    print("the operation is succssful")
