s1={'a','e','i','o','u','A','E','I','O','U'}
s2=set()
str="geeksforgeeks"
listconv = list(str)
print(listconv)

for i in listconv:
    if i in s1:
        s2.add(i.lower())
print(s2)
length = len(s2)

if length == 5:
    print("string is accepted")
else:
    print("string is not accepted")

