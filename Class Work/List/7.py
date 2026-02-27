l=[]
while True:
    a=int(input("Enter 1 for Enque \nEnter2 Deque \nEnter 3 for Dispalying the que \nEnter 4 for Exit\n"))
    if a==1:
        b=int(input("Enter a number that you want to add in the list"))
        l.append(b)
    elif a==2:
        if len(l)>0:
            print(l[0],"is removed")
            l.pop(0)
        else:
            print("There  are no values in the que")
    elif a==3:
        print(l)
    elif a==4:
        break
print(l)
