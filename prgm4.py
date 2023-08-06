#python prgm to swap two number
num1 = float(input("Enter a frist value:"))
num2 = float(input("Enter second value::"))

print("Before Swapping::")
print("first number : ", num1)
print("second number:", num2)

num1 , num2 = num2 , num1

print("After Swapping:")
print("frist number:", num1)
print("second number:", num2)
