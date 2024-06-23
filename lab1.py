def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)




try:
    additoin(10, 20)
except NameError as a:
    print(a)
except Exception as a:
    print("Failed operation of the type:",a)
else:
    print("The operation has been completed")