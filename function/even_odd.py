# Check number is even or odd
num1=int(input("Enter a number:"))
def check(num):
    if num % 2 != 1:
        print("Number is even:")
    else:
        print("Number is odd:")
check(num1)