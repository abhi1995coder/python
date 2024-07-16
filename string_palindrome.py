#program to check whether entered string is palindrome or not
s=input("enter the string to check")
k=len(s)
x=0
c=0
while x<k/2:
    if s[x]!=s[k-1]:
        c=c+1
        break
    
    x=x+1
    k=k-1
if c==0:
    print("string is palindrome")
else:
    print("string is not plaindrome")        