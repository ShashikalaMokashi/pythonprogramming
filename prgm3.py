#python progm on quadratic 
import cmath
a = float(input("Enter a value::"))
b = float(input("Enter b value::"))
c = float(input("Enter c value::"))

dis = (b**2) - (4*a*c)

solution1 = (-b + cmath.sqrt(dis)) / (2*a)
solution2 = (-b - cmath.sqrt(dis)) / (2*a)

print("The solution are:")

print("X1 = ", solution1)
print("X2 = ", solution2)
