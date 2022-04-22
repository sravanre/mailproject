newfile = open('newoutput.txt', 'a+')
file = open('TWSmapJobNames.txt', 'r')
 
line1 = file.readlines()

for i in line1:
    if i.rstrip():
        newfile.writelines(i)

newfile.close()