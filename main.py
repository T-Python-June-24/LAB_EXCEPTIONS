def additoin(x, y):
    try:    
        x = 10
        y = 20
        print("Addition:", x + b)
    except NameError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("The Operation is Successful")

additoin(10, 20)

