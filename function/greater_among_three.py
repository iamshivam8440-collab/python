# Find greater among three number
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))

# create function --> no returntype with parameter
def greater(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is greater:")
    elif num2>num1 and num2>num3:
        print(num2,"is greater:")
    elif num3>num1 and num3>num1:
        print(num3,"is greater:")
    else:
        print(num1,num2,num3,"is equal:")

# function call
greater(num1,num2,num3)    