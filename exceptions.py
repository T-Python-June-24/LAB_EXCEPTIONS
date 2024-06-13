def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + y)
        print("The operation is successful")
    except NameError as e:
        print(f"The operation failed {e}")

additoin(10, 20)
