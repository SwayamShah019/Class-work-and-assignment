#Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos.
import random
gen=[]
p=[]
n=[]
for i in range(30):
    a=random.randint(-100,100)
    gen.append(a)
    if a>0:
        p.append(a)
    elif a<0:
        n.append(a)
print("List containing all 30 integers: ",gen,"\nList containig all +ve integers from first list: ",p,"\nList containing all -ve integers from first list: ",n)
    
