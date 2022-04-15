


word = 'STATUS(E)'

with open(r'/var/tmp/DP5PLST1.TXT', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        if line.find(word) != -1:
            #print(word)
            print(line)

