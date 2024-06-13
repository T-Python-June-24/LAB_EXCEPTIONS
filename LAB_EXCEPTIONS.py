
'''
## Below you have a code that raises an exception , using what you learned do the following:


- Find what type of exception is raised.

- Hanlde the exception in try..except 

- If operation successful , print "the operation is successful"

- if operation fails, handle the specific exception that is raised , and print a relevant message.
```
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)
```


'''

class TestRaised(Exception):
    """Ops something went wrong...."""

def additoin(x: int, y: int) -> int:
    try:
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TestRaised("Inputs must be integers.")
        print("Addition:", x + b)
        print("The operation is successful")
    except TestRaised as e:
        print(f"TestRaised Exception occurred: {e}")
        print("The operation failed")
    except NameError as e:
        print(f"A NameError occurred: {e}")
        print("The operation failed")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("The operation failed")
    else:
        print("The operation is successful")

try:
    additoin(int(input("Enter a number 1: ")), int(input("Enter a number 2: ")))
except ValueError as e:
    print(f"A ValueError occurred: {e}")
    print("Please enter valid integers.")


#! another way to handle the exception
# def additoin(x, y):
#     try:
#         x = 10
#         y = 20
#         print("Addition:", x + b) 
#         print("The operation is successful")
#     except NameError as e:
#         print(f"A NameError occurred: {e}")
#         print("The operation failed")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         print("The operation failed")

# additoin(10, 20)
