a=int(input("Enter marks for 1st Subject: "))
b=int(input("Enter marks for 2nd Subject: "))
c=int(input("Enter marks for 3rd Subject: "))
total=a+b+c
avg=total/3
print("Total Marks: ",total,"\nAverage Marks: ",avg)
if a<=39:
    print("You had failed in 1st Subject")
if b<=39:
    print("You had failed in 2nd Subject")
if c<=39:
    print("You had failed in 3rd Subject")

if a>0 and a<=39:
    print("You had F Grade in 1st Subject")
elif a>=40 and a<=44:
    print("You had P Grade in 1st Subject")
elif a>=45 and a<=49:
    print("You had C Grade in 1st Subject")
elif a>=50 and a<=54:
    print("You had B Grade in 1st Subject")
elif a>=55 and a<=59:
    print("You had B+ Grade in 1st Subject")
elif a>=60 and a<=69:
    print("You had A Grade in 1st Subject")
elif a>=70 and a<=79:
    print("You had A+ Grade in 1st Subject")
elif a>=80 and a<=100:
    print("You had O Grade in 1st Subject")

if b>0 and b<=39:
    print("You had F Grade in 2nd Subject")
elif b>=40 and b<=44:
    print("You had P Grade in 2nd Subject")
elif b>=45 and b<=49:
    print("You had C Grade in 2nd Subject")
elif b>=50 and b<=54:
    print("You had B Grade in 2nd Subject")
elif b>=55 and b<=59:
    print("You had B+ Grade in 2nd Subject")
elif b>=60 and b<=69:
    print("You had A Grade in 2nd Subject")
elif b>=70 and b<=79:
    print("You had A+ Grade in 2nd Subject")
elif b>=80 and b<=100:
    print("You had O Grade in 2nd Subject")

if c>0 and c<=39:
    print("You had F Grade in 3rd Subject")
elif c>=40 and c<=44:
    print("You had P Grade in 3rd Subject")
elif c>=45 and c<=49:
    print("You had C Grade in 3rd Subject")
elif c>=50 and c<=54:
    print("You had B Grade in 3rd Subject")
elif c>=55 and c<=59:
    print("You had B+ Grade in 3rd Subject")
elif c>=60 and c<=69:
    print("You had A Grade in 3rd Subject")
elif c>=70 and c<=79:
    print("You had A+ Grade in 3rd Subject")
elif c>=80 and c<=100:
    print("You had O Grade in 3rd Subject")