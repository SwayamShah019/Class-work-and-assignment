# Program to calculate sine of an angle using Taylor series expansion
a=float(input("Enter Value in degree"))
b=a*22/7/180
def f(x):
    y = 1
    for i in range(1,x+1):
        y=i*y
    return y
i=0
k=0
c=1

while c>0.0000000000000000000000001:
    c=(-1)**i*b**(2*i+1)/f(2*i+1)
    k+=c
    i+=1
    if c<0:
        c=(c**2)**1/2
print(k)
