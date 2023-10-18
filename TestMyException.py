class MyException(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

def func():
    try:
        func1()
    except MyException as e:
        print(e)
        raise e

def func1():
    e = MyException("My Exception")
    raise e

try:
    print("Before Call func")
    func()
    print("After Call func")
except MyException as e:
    print(e)
print("Goodbye")