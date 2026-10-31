number=int(input("Enter your number:"))
original=number
rev=0
while(number):
    rev=rev*10+number%10
    number//=10
if(rev==original):
    print("Number is palindrome:")
else:
    print("Number is not palindrome:")