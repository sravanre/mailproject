
file1 = open('result_TWS_Report.txt', 'r').readlines()
file2 = open('TWSmapJobNames.txt', 'r').readlines()

# print(file1)

# print(file2)
for j in file2:
    for i in file1:
        if i.strip() in j:
            # print(j.strip().split(','))
            k = j.strip().split(',')
            print(k[1])

# file1.close()
# file2.close()