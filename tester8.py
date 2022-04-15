# error code is '23' that we are finding 

#check = '23'
with open(r"/var/tmp/test.csv", 'r') as fp:
    for l_no, line in enumerate(fp):
        for check in range(20, 29, 1):
            print(check)
            type(check)

        # search string
            if str(check) in line:
                #print('string found in a file')
                #print('Line Number:', l_no)
                #print('Line:', line)
                #print(line.strip())
                #don't look for next lines
                line1=line.strip()
                line2=line1.split(',')
                if check in line2:
                    print(line2[1])
