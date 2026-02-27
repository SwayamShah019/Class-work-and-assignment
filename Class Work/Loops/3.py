# Program to count the number of alphabets and digits in a string
a=input("Enter a string ")
c=0
d=0
for ch in a:
    if ch.isalpha()==True:
        c=c+1
for el in a:
    if el.isdigit()==True:
        d=d+1

print("No. of alphabets:",c)
print("No. of digits:",d)
