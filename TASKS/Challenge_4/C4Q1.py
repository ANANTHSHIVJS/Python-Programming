# Write a function which would divide two numbers, design the
# function in a manner that it handles the divide by zero exception

try:
    a=4
    b=0
    div=a/b
    print("Divided value is",div)

except:
    print("Division Error Occoured")

finally:
    print("am finally")