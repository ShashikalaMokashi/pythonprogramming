def calculate_gcd(a,b):
    while b != 0:
        a , b = b, a%b
    return a
def calculate_lcm(a,b):
    gcd = calculate_gcd(a,b)
    lcm =(a*b) // gcd
    return lcm
num1 = int(input("enter a 1st number"))
num2 = int(input("enter a 2st number"))

gcd = calculate_gcd(num1, num2)
print("The gcd of", num1 , "and" ,num2 , "is" ,gcd)

lcm = calculate_lcm(num1, num2)
print("The lcm of", num1 , "and" ,num2 , "is" ,lcm)

