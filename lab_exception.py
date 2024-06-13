def additoin(x, y):   
        x = 10
        y = 20
        print("Addition:", x + b)
try:
    additoin(10, 20)
except NameError as e:
        print("Error: try again")
        print(e)
except Exception as e:
        print("Error:", e)
else:
        print("Successful")
