list = [10, 20, 30, 40, 50]
sum = 0

for i in range (1,len(list)+1):
    list[i-1]=sum+list[i-1]
    sum=list[i-1]
print(list)
