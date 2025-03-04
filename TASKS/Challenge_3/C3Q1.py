# Create a function , and calculated using the formula:
# Final Price(FP) = (Product Price of of X )/(Product Price of Y)^2.
# Write python code which can accept the price X and price of Y of a
# Product and calculate the FP. Note: Make sure to use a function
# which accepts the X and Y values and returns the FP value.

def FP(x,y):
    result=((x/y)**2)
    return result
x=int(input("Enter the value of X : "))
y=int(input("Enter the value of Y : "))
print("The Final Price of Porduct is : ",FP(x,y))
