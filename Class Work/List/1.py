import random
odd=[]
even=[]
o=0
e=0
while o+e<9:
    a=random.randint(1,100)
    if a%2==0:
        if e<4:
            even.append(a)
            e+=1
    else:
        if o<5:
            odd.append(a)
            o+=1
print("Randomly Genrated odd list",odd,"Randomly Genrated even list",even)
odd[2]=even
print("After changing 3 term to of odd to list of even",odd)
odd=[odd[0], odd[1], *even, odd[3], odd[4]]
print("After flattern the list",odd)
odd.sort()
print("After sorting",odd)
