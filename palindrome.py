n3=int(input("enter (palindrome):"))
n4=n3
rev1=0
while n3!=0:
    rem1=n3%10
    rev1=(rev1*10)+rem1
    n3=n3//10
if(n4==rev1):
    print("palindrome")
else:
    print("not palindrome")
