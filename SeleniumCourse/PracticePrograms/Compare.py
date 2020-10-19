def file1():
    file = open("C:\\Users\\indrasen\\Downloads\\FilePractice\\TestFile.txt", "r")
    #print(file)
    #print(type(file))
    d = dict()
    #print(d)
    for line in file:
        line = line.strip()
        #print(line)
        line = line.lower()
        #print(line)
        words = line.split(" ")
        #print(words)
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    #print(d)
    sum1 = 0
    for key in list(d.values()):
        sum1 = sum1+key
    return(sum1)

def file2():
    file1 = open("C:\\Users\\indrasen\\Downloads\\FilePractice\\TestFile1.txt", "r")
    #print(file)
    #print(type(file))
    d = dict()
    #print(d)
    for line in file1:
        line = line.strip()
        #print(line)
        line = line.lower()
        #print(line)
        words = line.split(" ")
        #print(words)
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    #print(d)
    sum2 = 0
    for key in list(d.values()):
        sum2 = sum2+key
    return(sum2)

func_f1 = file1()
func_f2 = file2()
if func_f1 == func_f2:
    print("true")
else:
    print("false")
