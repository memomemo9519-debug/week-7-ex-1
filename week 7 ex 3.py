# append
#file = open('test-multi.txt', 'a')
#file.write("File Handling sent through Append..\n")
#file.close()

# With open
with open('test-multi.txt', 'r') as file:
    data = file.read()
print(data)