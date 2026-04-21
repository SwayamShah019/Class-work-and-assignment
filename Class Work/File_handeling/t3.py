#WAP to copy content frome one file and past in to other file
import os, sys
f1 = input("Enter a file name to read the content")
f2 = input("Enter the file name to write a content.")
if os.path.isfile(f1):
    fp1=open(f1,"r")
else :
    print("File doesnot exist")
    sys.exit()
fp2=open(f2,"w")
ch=fp1.read()
fp2.write(ch)
fp1.close()
fp2.close()
