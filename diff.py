


file1 = 'result_TWS_Report.txt'
file2 = 'TWSmapJobNames.txt'

f1 = open(file1)
#f2 = open(file2)

lines1 = f1.readlines()
#lines2 = f2.readlines()


##print(lines1)
new_file11 = open("mera.txt", "a+")
for i in range(len(lines1)):
    # print(i)
    # print(str(lines1[i].strip()))
#while i < len(lines1):
    #
    with open(file2, 'r') as fp:
        for l_no, line in enumerate(fp):
            #print(type(line))
            for text in lines1:
                if text in line:
                    print(line)
            #  if str(lines1[i]) in line:
                # print(line)
                # new_file11.writelines(line)

new_file11.close()
            # print(line)
            # print(lines1[3])      # this shows both are string  , i am missing somethign here  



            # if lines1[i] in line:
            #     print(line)
            #print(lines1[i])
            #if str(i) in line:
                

            # if "PLPAACDUNITFUND" in line:
            #     print(line)
        
            # print(line)
            # if str(lines1[i]) in line:
            #     #print(lines1[i])
            #     print(line.strip())


        # if str(lines1) in line:
        #     print(line)

# i = 0
# f1.seek(0)
# f2.seek(0)

# for line1 in ):
#     if lines1[i] in lines2[i]:
#         print(lines1[i])
#     i = i+1

# f1.close()
# f2.close()