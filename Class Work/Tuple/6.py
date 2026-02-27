#Modify an element of a tuple by creating a new tuple
a=(12, 21, 32, 56, 68, 65, 65, 32, 36, 45)
print(a)
b=int(input("Enter a number that you want to change" ))
c=int(input("Enter a number that you want to change to "))
d=list(a)
d[a.index(b)]=c
d=tuple(d)
print(d)
