#a = "Geeks for Geeks"
a = "apple banana mango"
#b = "Learning from Geeks for Geeks"
b = "banana fruits mango"

a1 = a.split(" ")
b1 = b.split(" ")
c1 = a1+b1

list = []

for i in c1:
    if c1.count(i)==1:
        list.append(i)
print(list)
