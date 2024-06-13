
# Find what type of exception is raised.
# Hanlde the exception in try..except
# If operation successful , print "the operation is successful"
# if operation fails, handle the specific exception that is raised , and print a relevant message.


def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b) # for handiling i should replace b with y 


try:

    additoin(10,20)


except NameError as e:

    print(e)

except Exception as e:
    print("somthing went wrong.. ", e)

else :

    print("the operation is successful")
    
