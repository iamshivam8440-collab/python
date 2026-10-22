dict={
    #"Keys":"value",
    "Hindi":"kahani",
    "English":"Poetry",
    "C":"Yashwant",
    "ANSI C":"B balagurusamy",
    "C++":"E balagurusamy",
}

# print keys of dictionary
print(dict.keys())

# print value of dictionary 
print(dict.values())

# print the items of dict ("keys":"value")
print(dict.items())

# update dict
updatedict={
    "Ramu":"Friend",
    "Shyam":"Dost"
}
dict.update(updatedict)
print(dict)

# return error if keys is not present
print(dict.get("Hello")) # --> return None key is not presnt in dict
print(dict.get("Hindi")) # --> return value of keys