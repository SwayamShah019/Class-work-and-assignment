b=0
g=0
lst=[("Swayam",),"Riya", ("Meet",)]
for i in lst:
    if isinstance(i,tuple):
        b=b+1
    else:
        g=g+1
print(b,g)
