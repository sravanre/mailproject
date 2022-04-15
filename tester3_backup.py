checkE= 'STATUS(E)'
checkW= 'STATUS(W)'
checkERR = 'ERR'

with open(r"/var/tmp/DP5PLST1.TXT", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if checkE in line:
            #print('string found in a file')
            #print('Line Number:', l_no)
            #print('Line:', line)
            print(line.strip())
            # don't look for next lines
        if checkW in line:
            print(line.strip())
        if checkERR in line:
            print(line.strip())
            
