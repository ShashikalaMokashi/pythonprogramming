#python program to display multiplication table
num = int(input("Enter the number:"))

print(f"Multiplication table for {num}:")
for i in range(1,11):
    result = num * i 
    print(f"{num} x {i} = {result}")
