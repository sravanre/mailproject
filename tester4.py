
with open(r"/var/tmp/test.csv", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if str(23) in line:
            #print('string found in a file')
            #print('Line Number:', l_no)
            #print('Line:', line)
            print(line.strip())
            # don't look for next lines
