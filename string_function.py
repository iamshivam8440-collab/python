info="good morning, My self Shivam chaurasiya. I am from Handia, Prayagraj. Today, I start learning python"
# string function
print("Length of string:",len(info)) 
print("End with :",info.endswith("hello"))
print("End with :",info.endswith("python"))
print("Count character in string:",info.count("i")) #count i in string
print("Capatilize of first string:",info.capitalize()) #good-->Good
# hello not present in string return(-1) if present return the index of first occurence
print("Find the string:",info.find("hello"))
# replace Shivam --> Nitin
print("New string is:",info.replace("Shivam","Nitin")) 