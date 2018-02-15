from numpy.linalg import inv



x,y = float(input("Enter the value of x: ")),int(input("Enter the value of y: "))
print("The value of x is",x)
print("The value of y is",y)

#arithmetic
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)

x+=1
y//=2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)

x,y=y,x

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)

#Questions for Brian Hill:
#about the import statemants, why is import numpy not working?
