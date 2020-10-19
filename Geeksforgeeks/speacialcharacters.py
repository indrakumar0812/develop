str =input("enter the string:")

regrex="[@_!#$%^&*()<>?/\|}{~:,]"

for i in str:
    if i in regrex:
        print("string accepted")
        break
else:
    print("string is not accepted")
