#write a python prgm to check the number is even or odd
number = int(input("Enter the no:"))

if (number % 2) == 0:
    result = "Even"
else:
    result = "odd"

print(f"the number {number} is {result}.")