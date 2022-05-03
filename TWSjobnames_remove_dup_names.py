## removing the white lines and removing the duplicate names also 

# newfile = open('newoutput_dups_removed.txt', 'a+')
# file = open('newoutput.txt', 'r')
 
# line1 = file.readlines()

# for i in line1:
#     if i.rstrip():
#         newfile.writelines(i)

# newfile.close()



### removing the duplicates lines on the text file itself

# lines_seen = set() # holds lines already seen
# outfile = open('newoutput_dups_removed.txt', "w")
# for line in open("newoutput.txt", "r"):
#     # print(line)
#     if line not in lines_seen: # not a duplicate
#         outfile.write(line)
#         lines_seen.add(line)
# outfile.close()

with open("newoutput.txt", "r") as f:
    linelist = f.readlines()
    print(len(linelist))

R = []
for line in linelist:
    if line not in R:
        R.append(line)

with open("temp_line.txt", "w") as f:
    for line in R:
        f.write(line)







