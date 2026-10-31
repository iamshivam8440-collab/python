number=int(input("Enter a number:"))
print("Table of ",number,"is:")
for i in range(1,11):
    # print(number,"x",i,"=",number*i)
    print(f"{number} x {i} = {number*i}") # formatting string