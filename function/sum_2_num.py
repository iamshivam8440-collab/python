# Write a function that return the sum of two number.
num1=int(input("Enter first number:"))
num2=int(input("Enter second nuumber:"))
def sum(num1,num2):
    return num1+num2
temp=sum(num1,num2)
print("Sum of",num1,"and",num2,"is:",temp)