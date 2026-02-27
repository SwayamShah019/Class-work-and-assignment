import random
lst=[]
for i in range(20):
    a=random.randint(1,10)
    lst.append(a)
print(lst)
a=int(input("Enter a number"))
for i in range(20):
    if lst[i]==a:
        print(a,"is same as",i+1,"term in the list")
