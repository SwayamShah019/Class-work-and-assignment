# If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number.
def prime_factors(x):
    factors=[]
    i=2
    if x<=1:
        print("Factors not possibel")
    else:
        while i<=x:
            if x%i==0:
                factors.append(i)
                x=x/i
            else :
                i=i+1
    return factors
a=int(input("Enter a integer to find its prime factors"))
print(prime_factors(a))
