#Accept two sets from the user.
# Write a program to check:
#1. Whether first set is subset of second.
#2. Whether second is superset of first.
#3. Whether both sets are equal.
s1=set()
s2=set()
while True:
    a=int(input("Enter 1 if you want to add element in set 1 or press 2"))
    if a==1:
        b=int(input("Enter the number"))
        s1.add(b)
    elif a==2:
        break
while True:
    a=int(input("Enter 1 if you want to add element in set 2 or press 2"))
    if a==1:
        b=int(input("Enter the number"))
        s2.add(b)
    elif a==2:
        break
print(s1, s2)
if s1 <= s2:
    print("Yes 1st Set is subset of 2nd")
else:
    print("No 1st is not subeset of 2nd")
if s2 >= s1:
    print("Yes 2nd is Superset of 1st")
else:
    print("No 2nd is not Superset of 1st")
if s1 == s2:
    print("Yes 1st and 2nd set are equal")
else:
    print("No 1st and 2nd set are equal")
