# Write a program that defines a function count_alpha_digits() that accepts a string and calculates the number of alphabets and digits in it. It should return these values as a dictionary.
def count_alpha_digits(s):
    alpha_count=0
    num_count=0
    alpha_digits={}
    for i in s:
        if i.isalpha():
            alpha_count+=1
        elif i.isdigit():
            num_count+=1
    alpha_digits["alpha_count"]=alpha_count
    alpha_digits["num_count"]=num_count
    return alpha_digits
a=input("Enter a string here")
print(count_alpha_digits(a))
