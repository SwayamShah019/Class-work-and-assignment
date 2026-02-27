a=input("Enter a string ")
b=input("Enter a string that you want to find that it is present in above string or not ")
if a.find(b)==-1:
    print("No",b,"is not present in the first string you entered")
else:
    print("Yes",b,"is present in the first string you entered")
