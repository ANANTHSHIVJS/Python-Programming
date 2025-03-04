#Simple Interst using function

def simple(p,n,r):
    si=((p*n*r)/100)
    return si
p=int(input("Enter the Principal        : ")) # Principal/ Initial Money
n=int(input("Enter the Number of years  : ")) # Time / Number of Years
r=int(input("Enter the Rate of interest : ")) # Rate of interest
print("The simple interest is : ",simple(p,n,r))