list = [2,4,9,10,5,7]
maxi= max(list[0],list[1])
secondmax = min (list[0],list[1])

for i in range (2, len(list)):
    if list[i]>maxi:
        secondmax=maxi
        maxi=list[i]
    else:
        if list[i]>secondmax:
            secondmax=list[i]
print("the second largest number is:", secondmax)
