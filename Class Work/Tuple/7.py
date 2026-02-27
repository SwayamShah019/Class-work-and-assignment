#Delete an element of a tuple by creating a new tuple.
a=(4,5,656,65,565,475,545,44,244,55,45,54)
print(a)
b=int(input("Enter the number that you want to delete"))
a=list(a)
a.remove(b)
a=tuple(a)
print(a)
