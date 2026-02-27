#Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.

date1=(1, 2, 2005)
date2=(3, 5, 2010)
c=(date1[2]-1)*365
d1=c+(date1[2]-1)//4
d=(date2[2]-1)*365
d2=d+(date2[2]-1)//4
n=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
d1=d1+n[date1[1]-1]+date1[0]
d2=d2+n[date2[1]-1]+date2[0]
if date1[2]%4==0 and date1[1]>2:
    d1=d1+1
if date2[2]%4==0 and date2[1]>2:
    d2=d2+1
print(abs(d2-d1))
