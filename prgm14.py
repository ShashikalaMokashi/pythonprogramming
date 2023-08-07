#linear equation

n = int(input("enter a no of elements in an array:"))
array= []

for i in range(n):
    num=int(input("enter a no of elements {i+1}:"))
    array.append(num)

tar = int(input("enter an element to be searched:"))

found = False
index = -1

for i in range(n):
    if array[i] == tar:
        found=True
        index=i
        break

if found:
    print(f"element {tar} found at index {index}.")
else:
    print(f"element not fount")
