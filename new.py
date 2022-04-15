# error code starts with the 2X series that we are finding 

check = ['21', '22', '10', '23', '24', '25', '26', '27', '28', '29']
with open(r"/var/tmp/test.csv", 'r') as fp:
    for l_no, line in enumerate(fp):
        for x in check:

        # search string
            if str(x) in line:
                #print('string found in a file')
                #print('Line Number:', l_no)
                #print('Line:', line)
            #print(line.strip())
            # don't look for next lines
                line1=line.strip()
                line2=line1.split(',')
                if x in line2:
                    #print(line2)
                    print(line2[1])
