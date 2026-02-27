import random
lst=[]
for i in range(50):
    a=random.randint(1,30)
    lst.append(a)
print(lst)
j=0
k=1
while j<len(lst)-1:
    k=j+1
    while k<len(lst):
        if lst[j]==lst[k]:
            lst.pop(k)
        else:
            k=k+1
    j+=1
print(lst)
