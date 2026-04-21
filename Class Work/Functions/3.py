# Write a program that defines a function create_array() to create and return a 3D array whose dimensions are passed to the function. Also initialize each element of this array to a value passed to the function. e.g. create_array(3,4,5,n) where first three arguments are 3D array dimensions and 4 th value is for initialing each value of the 3D array
def create_array(a,b,c,d):
    array=[d]*a
    for i in range (c):
        for i in range(b):
            print(array, end=" ")
        print("")
create_array(2,3,4,10)
