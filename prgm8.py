#write a python prgm to find factorial of number
num = int(input("Enter a number::"))
fact = 1
if num >= 1:
    for i in range(1, num+1):
        fact = fact * i
print(f"factorial of number is = ", fact)

