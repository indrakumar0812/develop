a = [0,4,2,23,-1,34]

first_min = min(a[0],a[1])
second_min = max(a[0],a[1])

#print(min_a)
for i in range (2,len(a)):
    if a[i]<first_min:
        second_min=first_min
        first_min=a[i]
    elif a[i]<second_min:
        second_min=a[i]

print("second min no. is:",second_min)