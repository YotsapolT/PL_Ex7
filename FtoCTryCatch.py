try:
    print("Please enter degree in fahrenheit ", end="")
    fahrenheit = input()
    fahrenheit_FLOAT = float(fahrenheit)
except ValueError:
    print("Your input is not valid: ", end="")
    print(ValueError)    
finally:
    print("Finally")
print("Good Bye")