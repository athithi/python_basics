num=int(input("Enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#person eligible to vote
age=int(input("Enter age:"))
if age>18:
    print("eligible")
else:
    print("not eligible")

#largest of 2 numbers
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if num1>num2:
    print(num1,"is larger")
else:
    print(num2,"is larger")

#grade student
mark=int(input("Enter mark:"))
if mark>=90:
    print("Grade:A")
elif mark>=80:
    print("Grade:B")
elif mark>=70:
    print("Grade:C")
elif mark>=60:
    print("Grade:D")
else:
    print("Grade:F")

#electricity bill
unit=int(input("Enter units:"))
if unit<=100:
    bill=unit
elif unit<=200:
    bill=100+(unit-100)*2
elif unit<=300:
    bill=100+(100*2)+(unit-200)*4
else:
    bill=100+(100*2)+(100*4)+(unit-300)*5
print("bill=",bill)

#1 to n
n=int(input("enter n:"))
for i in range(1,n+1):
    print(i)

#1 to 50 even
for j in range(0,50,2):
    print(j)

#factorial
n1=int(input("enter (factorial):"))
fact=1
for i in range(1,n1+1):
    fact=fact*i
print("factorial=",fact)

#reverse
n2=int(input("enter (reverse):"))
rev=0
while n2!=0:
    rem=n2%10
    rev=(rev*10)+rem
    n2=n2//10
print("reverse=",rev)

#palindrome
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

#add fun
def mysum(x,y):
    return x+y
n5=66
n6=33
print("sum=",mysum(n5,n6))

#larger fun

def mymax(a,b):
    if a>b:
        print(a,"is larger")
    else:
        print(b,"is larger")
num11=int(input("Enter num1:"))
num12=int(input("Enter num2:"))
mymax(num11,num12)

#fact fun
def fact(c):
    fact=1
    for i in range(1,c+1):
        fact=fact*i
    print("factorial=",fact)
n13=int(input("enter (factorial):"))
fact(n13)


#prime fun
def prime(d):
    if d<=1:
        return False
    for i in range(2,d):
        if d%i==0:
            return False
    return True
n14=int(input("enter number: "))
print(prime(n14))

#calc
g=10
h=11
def add(e,f): return e+f
def sub(e,f): return e-f
def mul(e,f): return e*f
def div(e,f): return e/f
print(add(g,h))
print(sub(g,h))
print(mul(g,h))
print(div(g,h))

#list
mylist=[10,20,30,40,50]
for x in mylist:
    print(x)

#list sum
nums=[10,20,30,40]
print(sum(nums))

#max min
print("Max:",max(nums))
print("Min:",min(nums))

#remove duplicate
nums1=[1,2,2,3,4,4,5]
nums2=list(set(nums1))
print(nums2)

#to do list
tasks=[]
while True:
    task=input("Enter task or quit: ")
    if task=='quit':
        break
    tasks.append(task)
    print("to do list:", tasks)




