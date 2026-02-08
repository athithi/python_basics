def fact(c):
    fact=1
    for i in range(1,c+1):
        fact=fact*i
    print("factorial=",fact)
n13=int(input("enter (factorial):"))
fact(n13)
