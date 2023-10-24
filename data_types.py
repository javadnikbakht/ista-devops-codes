a = 12 # int
a = -3.5 # float
a = True # False # bool
a = 2 - 3j # complex

a = "blob12sfasdf" # 'blobblob' """ blob forlan sdfasdf""" # string

x = a[2:3] # slicing

# print(x)
# print(type(x))
# print(len(x))

a = [1, -3.4, True, "salam"] # list


a.pop() # list methods
print(a, end="\n\n") 
print(id(a))

a.append("apple")
print(a, end="\n\n")
print(id(a))

a.insert(0, 3-2j)
print(a, end="\n\n")
print(id(a))

################################################
# tuples

a = (1, 2, 3, 4)
print(a)
print(id(a), end="\n\n")

a = a + (5,)
print(a)
print(id(a), end="\n\n")
print(a.count(5))
print(a.index(5))

################################################

# dictionary

arman_info = {
    "name": "Arman",
    "lname": "Beykian",
    "age": 36
}

print(arman_info["lname"])
# print(arman_info["code_melli"]) # raise error
print(arman_info.get("code_melli", "1234567891"), end="\n\n")

print(arman_info.get("age", 120))

print(list(arman_info.keys()))
print(list(arman_info.items()))

arman_info.clear()
print(arman_info)

################################################

# set

alist = [1,1,2,3,5,2,3]
a = set(alist)
b = {1, True, "salam"}
print(a)


################################################

# casting

a  = 12
b = "12"

c = int(b) # cast b to int
d = str(a) # cast a to str

z  = (1, 2, 3)
x = list(z) # cast z to list

# False Values in casting to bool
[]
()
0
0.0
{}

