'''test = "Java is best"
test_list = test.split()
print(test_list)
print(type(test_list))

a = test_list[::-1]
print(' '.join(a))'''

'''a = "Army".lower()
b= "Macy".lower()

list_a = list(a)
list_b = list(b)

print(list_a)
print(list_b)

count=0

for i in range(len(list_a)):
    if list_a[i] in list_b:
        count+=1
if count == len(list_a):
    print("True")
else:
    print("False")'''

a = "Programming"
x=a.count("m")
c="m"
b = list(a)

for j in range (x):
    for i in b:
        if i =='m':
            b.remove(i)

print(''.join(b))




