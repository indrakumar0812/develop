list = [2, 7, 5, 64, 14]
list1 =[]
count_odd=0
count_even=0
for i in list:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1

print("no. of odd numbers are", count_odd)
print("no. of even numbers are", count_even)

