# Assume you want to build two functions for discounting products on
# a website. Function number 1 is for student discount which discounts
# the current price to 10%. Function number 2 is for additional discount
# for regular buyers which discounts an additional 5% on the current
# student discounted price. Depending on the situation, we want to be
# able to apply both the discounts on the products. Design the above
# two mentioned functions and apply them both simultaneously on
# the price.

def student(p):
    return (p-p*(10/100))
def regular(p):
    return (p-p*(5/100))
p=int(input("Enter the current price : "))
q=input("Are you a student : ")
if q=="yes":
    print("The discount price is : ",student(p))
elif q=="no":
    print("The discount price is : ",regular(student(p)))
else:
    print("Please enter a valid answer")