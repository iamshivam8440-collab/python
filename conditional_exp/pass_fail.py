# Find out whether a student is pass or fail
subj1=int(input("Enter 1st subject marks:"))
subj2=int(input("Enter 2nd subject marks:"))
subj3=int(input("Enter 3rd subject marks:"))

if(subj1<=33 or subj2<=33 or subj3<=33):
    print("Fail")
else:
    print("Pass")
