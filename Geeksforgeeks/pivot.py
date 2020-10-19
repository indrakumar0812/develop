list=  [1,3,4,1,8] #17
#total sum-leftsum-i=leftsum

total_sum=0
for i in list:
    total_sum+=i

left_sum=0
for i in list:
    if (total_sum-left_sum-i)==left_sum:
        print("the pivot element is:",i)
        break
    left_sum += i
else:
    print("no pivot element")


