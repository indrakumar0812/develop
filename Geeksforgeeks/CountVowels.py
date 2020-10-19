s1=['a','e','i','o','u','A','E','I','O','U']
s2 =[]
str="Hello World"
listconv = list(str)
for i in listconv:
    if i in s1:
        s2.append(i.lower())
print(len(s2))



