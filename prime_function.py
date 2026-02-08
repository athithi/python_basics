def prime(d):
    if d<=1:
        return False
    for i in range(2,d):
        if d%i==0:
            return False
    return True
n14=int(input("enter number: "))
print(prime(n14))
