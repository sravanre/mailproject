from fpdf import FPDF
import os
import pathlib


#checkE= 'STATUS(E)'
checkW= 'STATUS(W)'
#checkERR = 'ERR'
filepath = 'DP5PLST1.TXT'


# removing the files before every new execution 

textfile = pathlib.Path("result_TWS_Report.txt")
pdffile = pathlib.Path("PDF_TWS_report.pdf")
comparedfile1 = pathlib.Path("compared_output_2files.txt")

if textfile.exists():
    os.remove("/mnt/d/mail_project/result_TWS_Report.txt")
if pdffile.exists():
    os.remove("PDF_TWS_report.pdf")
if comparedfile1.exists():
    os.remove("compared_output_2files.txt")


my_file = open("/mnt/d/mail_project/result_TWS_Report.txt", "a+")
with open(filepath, 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        # if checkE in line:
        #     #print('string found in a file')
        #     #print('Line Number:', l_no)
        #     #print('Line:', line)
        #     print(line.strip())
        #     # don't look for next 
            
        #     my_file.writelines(line)
            

        if checkW in line:
            #print(line.strip().split(' '))
            line1 = line.strip().split(' ')
            line2 = line1[3]
            line3 = line2[5:-1]

            print(line3)

            
            my_file.writelines(line3)
            my_file.writelines('\n')
        # if checkERR in line:
        #     print(line.strip())
            
        #     my_file.writelines(line)

my_file.close()


#comparing the two generated files and writing the output into the batch report on a new lines , file: diff1.py

compared_output_2files = open("compared_output_2files.txt", "a+")
compared_output_2files.write("\t\t\t\t:::::WAITING JOBS:::::")
compared_output_2files.write('\n')
file1 = open('result_TWS_Report.txt', 'r').readlines()
file2 = open('TWSmapJobNames.txt', 'r').readlines()

# print(file1)

# print(file2)
for j in file2:
    for i in file1:
        if i.strip() in j:
            #print(j.strip())
            # print(j.strip().split(','))
            k = j.strip().split(',')
            print(k[1] + 'BatchJob')
            compared_output_2files.writelines(k[1] + 'BatchJob')
            compared_output_2files.writelines('\n')

compared_output_2files.close()






# file_1 = open('result_TWS_Report.txt', 'r')
# file_2 = open('TWSmapJobNames.txt', 'r')

# file_1_line = file_1.readlines()
# file_2_line = file_2.readlines()

# # print(file_1_line)
# print('\n')
# print(file_2_line)


# for i in file_1_line:
#     if i in file_2_line:
#         print(file_2_line)


# #############################
# # save FPDF() class into 
# # a variable pdf
# pdf = FPDF()   
   
# # Add a page
# pdf.add_page()
   
# # set style and size of font 
# # that you want in the pdf
# pdf.set_font("Arial", size = 15)

# output_file = open("/mnt/d/mail_project/result_TWS_Report.txt", "r")

# for pdf_line in output_file:
#     #pdf.cell(200, 10, txt = pdf_line,border= 100, ln = 1, align = "L")
#     #pdf.Cell(200, 10, txt = pdf_line, ln = 1, align = "L")
#     pdf.multi_cell(200, 10, txt = pdf_line, align = "L")

# pdf.output("PDF_TWS_report.pdf")

          
