a=[2,3,5,1,6,1,9,4]
b=[]
while len(a)>0:
    b.append(min(a))
    a.remove(min(a))
print(b)
