import json
f = open("Sampledata","w+")
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
json.dump(lst,f)
f.seek(0)
inlst = json.load(f)
print(inlst)
f.close()
