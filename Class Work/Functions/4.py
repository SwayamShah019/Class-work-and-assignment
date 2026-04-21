# Write a program that defines a function sum_avg() to accept marks of five subjects and calculates total and average.It should return directly both values
def sum_avg():
    ref=0
    for i in range(5):
        a=int(input("Enter marks of a diifrent mSubject "))
        ref+=a
    return "Total marks:", ref, "Avg marks:", ref/5
print(sum_avg())
