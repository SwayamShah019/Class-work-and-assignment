# A palindrome is a word or phrase that reads the same in both directions. Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not. Ignore spaces and case mismatch while checking for palindrome.
def ispalindrome():
    s = input("Enter a string :")
    j = s.lower()
    j = j.replace(" ", "")
    t = ""
    for i in range(len(j)):
        t=t+j[-1*(i+1)]
    if j==t:
        return(s," is palinddrome")
    else :
        return(s," is not palindrome")
print(ispalindrome())
