#A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.
def binary(x):
    a=""
    if x<=0:
        print("Number you entered can not br turn in binary")
    else:
        while x!=0:
            a=str(x%2)+a
            x=x//2
    return a
a=int(input("Enter a number to convert it in binary"))
print(binary(a))
