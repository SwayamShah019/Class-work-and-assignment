# Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether a given string is pangram or not, through a user-defined function ispangram(). Test the function with “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very exquisite opal jewels”. Hint: use set() to convert the string into a set of characters present in the string and use <= to check whether lphaset is a subset of the given string.
def pangram():
    s=input("Enter String")
    ref=""
    ref_set={chr(i) for i in range(97,123)}
    ref_set2=set()
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            k=chr(ord(i)+32)
            ref=ref+k
        else:
            ref=ref+i
    for i in ref:
        ref_set2.add(i)
    if ref_set<ref_set2:
        return s,"is a pangram"
    else:
        return s, "is not a pangram"
print(pangram())
