def add(l,m):
    return l+m
def subtract(l,m):
    return l-m
def multiply(l,m):
    return l*m
def divide(l,m):
    return l/m
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
    choice=input("Enter choice(1/2/3/4):")
    if choice in('1','2','3','4'):
        l=float(input("Enter first number:"))
        m=float(input("Enter second number:"))
        if choice=='1':
            print(l,"+",m,"=",add(l,m))
        elif choice=='2':
            print(l,"-",m,"=",subtract(l,m))
        elif choice=='3':
            print(l,"*",m,"=",multiply(l,m))
        else:
            print(l,"/",m,"=",divide(l,m))
    else:
        print("Invalid input")
