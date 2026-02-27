# Program to check if a number is prime, composite, perfect, amstrong, palindrome and automorphic
a=int(input("Enter a integer"))
b=int(a**(1/2))
c=0
f=0
g=""
e=str(a)
if a==1:
    print("Not a prime number not a composite number")
for i in range(2,b+1):
    if a%i==0:
        print(a,"is composite number")
        break
    else:
        print(a,"is prime number")
        break
for i in range(1,a//2+1):
    if a%i==0:
        c=c+i
if c==a:
    print(a,"is perfect number")
else:
    print(a,"is not a perfect number")
for ch in str(a):
    f=f+int(ch)**3
if f==a:
    print(a,"is amstrong number")
else:
    print(a,"is not amstrong number")
for i in range(len(e)):
    g+=(e[(i+1)*(-1)])
if g==e:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")
if (a**2)%10==a%10:
    print(a,"is an automorphic number")
else:
    print(a,"is not an automorphic number")
