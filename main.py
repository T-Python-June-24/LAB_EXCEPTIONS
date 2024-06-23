def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
        print("The operation is successful")
    except NameError as e:
        print(f"Operation failed: {e}")

additoin(10, 20)