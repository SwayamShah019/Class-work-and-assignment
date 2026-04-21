#Write a function to create and return a list containing tuples of the form (x,x2,x3) for all x between 1 and given ending value (both inclusive).
def cube(x):
    cube=[]
    for i in range(x):
        ref=[]
        for j in range(3):
            ref.append((i+1)**(j+1))
        cube.append(tuple(ref))
        ref=list(ref)
    return cube
print(cube(5))
