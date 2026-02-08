n2=int(input("enter (reverse):"))
rev=0
while n2!=0:
    rem=n2%10
    rev=(rev*10)+rem
    n2=n2//10
print("reverse=",rev)
