# Program to calculate nCr and nPr
def f(x):
    y=1
    for i in range(1,x+1):
        y=i*y
    return(y)
n=int(input("Enter a number for n"))
r=int(input("Enter a number for r"))
print(n,"C",r,"=",f(n)/f(n-r)/f(r))
print(n,"P",r,"=",f(n)/f(n-r))
