#Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of uppercase and lowercase alphabets in it. It should return these values as a dictionary. Call this function for some sample string.
def count_lower_upper(x):
    upper_count=0
    lower_count=0
    strings={}
    for i in x:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    strings["uppercount"]=upper_count
    strings["lowercount"]=lower_count
    return strings
a=input("Enter para here")
print(count_lower_upper(a))
