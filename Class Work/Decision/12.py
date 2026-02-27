a=float(input("Enter the coordinate of the center of circle"))
b=float(input())
r=float(input("Enter the Radius of circle"))
x=float(input("Enter the coordinate of pint"))
y=float(input())
z=((a-x)**2+(b-y)**2)**1/2
if z<r:
    print("Point is inside the circle")
elif z=r:
    print("Point is on the Circle")
else :
    print("Point is outside the circle")
