def addition(x, y):   
    try:
        if not type(x) is int or not type(y) is int:
            raise Exception("That wasn't a valid input")
        elif x == 0 or y == 0:
            raise Exception("Zeros do nothing in Addition")
        else: 
            print("the operation is successful: ")
            print("the sum of {x} and {y} is ", x + y)

    except Exception as e:
        print(e)
        
addition(10,20)