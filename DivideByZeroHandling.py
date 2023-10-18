def quotient(numerator, denominator):
    try:
        return int(numerator / denominator)
    except ZeroDivisionError: 
        raise ZeroDivisionError

continueLoop = True
while continueLoop:
    try:
        print("Please enter an integer numerator: ", end="")
        numerator = input()
        numerator_INTEGER = int(numerator)
        print("Please enter an integer denominator: ", end="")
        denominator = input()
        denominator_INTEGER = int(denominator)
        quotient = quotient(numerator_INTEGER, denominator_INTEGER)
        print("Result: ", quotient)
        continueLoop = False
    except ValueError: 
        print("You must enter integers. Please try again.")
    except ZeroDivisionError: 
        print("Zero is an invalid denominator. Please try again.")

 