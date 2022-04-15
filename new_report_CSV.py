# error code starts with the 2X series that we are finding 
from fpdf import FPDF
import os
import pathlib
from os import initgroups


check_error = ['21', '22', '10', '23', '24', '25', '26', '27', '28', '29']  ## 10 status code is also added into the check as of now
inprogress = ['-1']



textfile = pathlib.Path("/mnt/d/mail_project/result_morning_batch_report.txt")
pdffile = pathlib.Path("/mnt/d/mail_project/Morning_batch_report.pdf")

if textfile.exists():
    os.remove("/mnt/d/mail_project/result_morning_batch_report.txt")
if pdffile.exists():
    os.remove("/mnt/d/mail_project/Morning_batch_report.pdf")




my_file = open("/mnt/d/mail_project/result_morning_batch_report.txt", "a+")
with open(r"/var/tmp/test.csv", 'r') as fp:
    print("\t\t:::ERROR JOB LIST:::")
    my_file.writelines("\t\t:::ERROR JOB LIST::::")
    for l_no, line in enumerate(fp):
        for x in check_error:

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
                    #print("::::ERROR job Report::::")
                    print(line2[1])
                    #print(line2[1])
                    my_file.write('\n')
                    my_file.writelines(line2[1])

with open(r"/var/tmp/test.csv", 'r') as fp:
    print('\n')
    print("\t\t::::INPROGRESS JOB LIST ::::::")
    my_file.writelines('\n')
    my_file.writelines("\t\t::::INPROGRESS JOB LIST ::::::")
    for l_no, line in enumerate(fp):
        for x in inprogress:
            if str(x) in line:
                line1=line.strip()
                line2=line1.split(',')
                if x in line2:
                    #print("::::ERROR job Report::::")
                    print(line2[1])
                    #print(line2[1])
                    my_file.write('\n')
                    my_file.writelines(line2[1])
my_file.close()




#### writing to a pdf file 


pdf = FPDF()   
   
# Add a page
pdf.add_page()
   
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)

output_file = open("/mnt/d/mail_project/result_morning_batch_report.txt", "r")

for pdf_line in output_file:
    pdf.cell(200, 10, txt = pdf_line,border= 100, ln = 1, align = "L")
    #pdf.Cell(200, 10, txt = pdf_line, ln = 1, align = "L")

pdf.output("Morning_batch_report.pdf")




