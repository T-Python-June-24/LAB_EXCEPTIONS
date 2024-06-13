def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except Exception as e:
    print(f"The Exepetion is: {e.__doc__}")
    print("make sure that you've defined the name correctly")
else:
    print("the operation is successful")