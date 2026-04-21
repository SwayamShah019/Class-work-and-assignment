#1. Two students choose subjects represented as sets:
#s1 = {'Math', 'Physics', 'Chemistry'} and s2 = {'Physics', 'Biology', 'Math'}
#Write a program to:
#1. Find common subjects.
#2. Find subjects taken by only first student.
#3. Find subjects taken by only second student.
#4. Find total unique subjects.

s1={"Maths", "Physics", "Chemistry"}
s2={"Biology", "Physics", "Chemistry"}
print(s1 & s2)
print(s1 - (s1 & s2))
print(s2 - (s1 & s2))
print(s1 | s2)
