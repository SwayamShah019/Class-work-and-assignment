# Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
f=[]
c=[]
# c=5/9*(f-32)
a="Yes"
while a=="Yes" or a=="yes":
    fs=float(input("Enter a tempraure in Fahrenheit: "))
    a=input("Do You want to continues Yes/No: ")
    f.append(fs)
for i in f:
    cs=5/9*(i-32)
    c.append(cs)
print("Corrosponding Temprature in Celcius: ",c)
    
