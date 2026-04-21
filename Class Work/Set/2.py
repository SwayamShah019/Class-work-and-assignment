#A website records visitor IDs for two different days as sets.
# Write a program to:
#1. Find visitors who visited both days.
#2. Find visitors who visited only one of the days.
#3. Find total unique visitors across both days.
#4. Find if all visitors who visited the website on first day also visited on the second day
Day1={1, 2, 6, 9, 8}
Day2={1, 3, 4, 6, 10}
print("Visitors id who visited bot the days", Day1 & Day2 )
print("Visitors id who visited only one of the day", (Day1 | Day2)-(Day1 & Day2))
print("Visitors id of unique visitors across both the days", Day1 |  Day2)
if Day1 == Day1 & Day2:
    print("Yes all the visitors visited Day1")
else:
    print("No all the visitors visited Day1")
