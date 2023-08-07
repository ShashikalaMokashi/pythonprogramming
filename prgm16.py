#sorted array
def insert_into_sorted_array(array,num):

    index = 0
    while index < len(array) and array[index] < num:
        index += 1
    
    array.insert(index,num)
n = int(input("enter no of elements in array:"))
array = []

for i in range(n):
    num = int(input("enter the  elements {i+1} :"))
    array.append(num)

num_to_insert =int(input("enter the number to be inserted:"))

insert_into_sorted_array(array, num_to_insert)

print("updated array:", array)
