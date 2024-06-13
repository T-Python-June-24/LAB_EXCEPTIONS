
# class UndefindException(Exception):
#     print("Name Error")

def additoin(x, y):   
    x = 10
    y = 20
    print("Addition:", x + b)   #NameError  name 'b' is not defined

try:
    additoin(10, 20)
except NameError as e:
    print(e)
    print("Name Error, a name of a varibale used is undefind !")
else :
    print("the operation is successful !!!")
