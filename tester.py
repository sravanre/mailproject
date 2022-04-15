

import re
import subprocess

string1 = 'Total'
textfile = open("/var/tmp/DP5PLST1.TXT", 'r')
filetext = textfile.read()
textfile.close()

##  matches = re.findall( , filetext)

#print(filetext)


#matches = re.search("(E)", filetext)
#print(matches)


#process = subprocess.run(['grep', '-w', '(E)', filetext], capture_output=True, text=True)



#match = re.search('STATUS', filetext)
#print(match)

for line in filetext:
    if string1 in line:
        print(line)
