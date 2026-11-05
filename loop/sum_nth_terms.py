# Sum of nth terms
number=int(input("Enter the number:"))
sum=0
for i in range(1,number+1):
    sum=sum+i
print("Sum of ",number,"terms is:",sum)