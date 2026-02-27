print("The Program is for 2D plane")
a=float(input("Enter the coordinates for first point"))
b=float(input())
x=float(input("Enter the coordinates for second point"))
y=float(input())
m=float(input("Enter the coordinates for third point"))
n=float(input())
j=((a-x)**2+(b-y)**2)**1/2
k=((a-m)**2+(b-n)**2)**1/2
l=((x-m)**2+(y-n)**2)**1/2
if j==k+l:
    print("The three poits are in line")
elif k==j+l:
    print("The three poits are in line")
elif l==j+k:
    print("The three poits are in line")
else:
    print("The three points are not in a line")

