a=int(input("enter  first side of triangle"))
b=int(input("enter  second side of triangle"))
c=int(input("enter  third side of triangle"))


print(f"sides of  triangle are -- a:{a} b:{b} c:{c}")


s=(a+b+c)/2             #s=semiperimeter  of  triangle
area=(s*(s-a)*(s-b)*(s-c))**0.5

print("area of  triangle is  %0.2f"%(area))


