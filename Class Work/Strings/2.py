a=input("Enter a string")
b=input("Press U for upper case Press l for lower case and press t for toogle case")
if b=="U":
    for ch in a:
        if ord(ch)>=97 and ord(ch)<=122:
            print(chr(ord(ch)-32), end="")
        else:
            print(ch, end="")
if b=="l":
    for ch in a:
        if ord(ch)>=65 and ord(ch)<=90:
            print(chr(ord(ch)+32),end="")
        else:
            print(ch,end="")
if b=="t":
    for ch in a:
        if ord(ch)>=65 and ord(ch)<=90:
            print(chr(ord(ch)+32),end="")
        elif ord(ch)>=97 and ord(ch)<=122:
            print(chr(ord(ch)-32), end="")
        else:
            print(ch, end="")


    


