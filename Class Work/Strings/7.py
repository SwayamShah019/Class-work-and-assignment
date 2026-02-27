a=input("Enter a string")
print("Length of string you entered: ",len(a))
v=0
for ch in a:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        v=v+1
print("There are ",v,"vowels in your entered string and ther are ",len(a)-v,"consonants in the enterd string")
