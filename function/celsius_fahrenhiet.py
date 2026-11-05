celsius=int(input("Enter temperature:"))
# function -> returntype with parameter
def temp(celsius):
    fahrenhiet=(9*celsius)/5+32
    return fahrenhiet
print("Temperature in fahrenhiet:",temp(celsius))
