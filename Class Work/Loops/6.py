# Program to print the time in 12 hour format
for h in range(24):
    if h==12:
        print("noon")
    elif h==0:
        print("midnight")
    else:
        print(h%12, end=" ")
    if h<12 and h>0:
        print("A.M")
    elif h>12 and h<24:
        print("P.M")
