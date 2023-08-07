#exception handling
try:

    x = int(input("enter a no:"))
    y = 10 / x
    print("result:",y)

except ValueError:
    print("invalid input. please enter valid no")

except ZeroDivisionError:
    print("cannot divide by zero")
    