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
