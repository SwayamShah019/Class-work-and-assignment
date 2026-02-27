#Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension).
import random
a1=random.randint(1,10)
a2=random.randint(1,10)
print(a1, a2)
l1=[random.randint(1,20) for i in range(a1)]
l2=[random.randint(1,20) for i in range(a2)]
print(l1, l2)
l3=[l1[i] for i in range(a1) if l1 not in l2]
l3=l3+[l2[i] for i in range(a2) if l2 not in l1]
print(l3)
