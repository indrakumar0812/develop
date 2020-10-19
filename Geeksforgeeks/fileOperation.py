with open('C:\\Users\\indrasen\\PycharmProjects\\PythonProgramExamples\\Geeksforgeeks\\test','r') as reader:
    content = reader.readlines()
    print(reversed(content))
    with open('C:\\Users\\indrasen\\PycharmProjects\\PythonProgramExamples\\Geeksforgeeks\\test','w') as writer:
        for line in reversed(content):
            writer.write(line)

