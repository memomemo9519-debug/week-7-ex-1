#'r': read by line
# [] = List
# () = Tuples
# {} = Dictionaries
#file = open('test.txt', 'r')
#lines = file.readlines()
#print(lines)
#file.close()

#w : Write multiple
file = open('test-multi.txt', 'w')
file.write("File Handling..\n")
file.writelines(["Java\n","Python\n",".NET"])
file.close()