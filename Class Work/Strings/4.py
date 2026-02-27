a=input("Enter Your string")
print("First character:",a[0],"Last character:",a[len(a)-1])
if len(a)%2!=0:
    b=int((len(a)-1)/2)
    print("Middle Character:",a[b])
