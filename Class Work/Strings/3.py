a=input("Enter a string")
i=0
b=len(a)
for i in range(b):
    print(a[(i+1)*-1],end="")
