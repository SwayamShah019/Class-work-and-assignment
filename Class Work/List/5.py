# A list contains 5 strings. Convert all these strings to uppercase.
s=["Swayam", "PDEU", "Computer", "Python", "Division-2"]
print(s)
n=0
for i in s:
    m=""
    for j in i:
        if ord(j)>=97 and ord(j)<=122:
            k=chr(ord(j)-32)
            m=m+k
        else:
            k=chr(ord(j))
            m=m+k
    s[n]=m
    n+=1
print(s)
