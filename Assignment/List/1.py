l=[]
while True:
    a=int(input("Enter 1 to add number in stack \nEnter 2 if you want to remove the previous element \nEnter 3 for Dispalying the Stack \nEnter 4 for Exit\n"))
    if a==1:
        b=int(input("Enter a number that you want to add in the list"))
        l.append(b)
    elif a==2:
        if len(l)>0:
            n=len(l)-1
            print(l[n],"is removed")
            l.pop(n)
        else:
            print("There  are no values in the que")
    elif a==3:
        print(l)
    elif a==4:
        break
print(l)
