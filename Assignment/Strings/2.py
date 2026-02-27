a=input("Enter a string ")
b=input("Enter a string that you want to remove from above string ")
c=len(b)
if a.find(b)==-1:
    print("No",b,"is not present in the first string you entered")
else:
    for ch in range(a.find(b)):
        print(a[ch],end="")
    for ch in range(a.find(b)+len(b),len(a)):
        print(a[ch],end="")
