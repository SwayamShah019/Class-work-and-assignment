# Program to print Fibonacci series up to n terms
n=int(input("Enter a number "))
print("0",end="")
i=1
k=0
j=0
while i<=n:
    print(",",i,end="")
    k=i
    i=i+j
    j=k
