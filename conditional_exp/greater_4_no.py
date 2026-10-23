# Greater among four number
number1=int(input("Enter 1st number:"))
number2=int(input("Enter 2nd number:"))
number3=int(input("Enter 3rd number:"))
number4=int(input("Enter 4th number:"))

if(number1>number4):
    f1=number1
else:
    f1=number4
if(number2>number3):
    f2=number2
else:
    f2=number3
if(f1>f2):
    print(f1,"is gerater")
else:
    print(f2,"is greater")