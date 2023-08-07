#positive and  negetive no

n = int(input("enter a no of elements in array:"))
array = []

for i in range(n):
    num = int(input("enter a element {i+1}:"))
    array.append(num)

positive_sum = 0
negative_sum = 0

for num in array:
    if num > 0:
        positive_sum  += num
    if num < 0:
        negative_sum += num

print("sum of +ve no =",positive_sum)
print("sum of -ve no =", negative_sum)