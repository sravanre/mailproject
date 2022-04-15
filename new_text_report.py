from fpdf import FPDF
import os
import pathlib


checkE= 'STATUS(E)'
checkW= 'STATUS(W)'
checkERR = 'ERR'
filepath = '/var/tmp/DP5PLST1.TXT'


# removing the files before every new execution 

textfile = pathlib.Path("/mnt/d/mail_project/result_TWS_Report.txt")
pdffile = pathlib.Path("PDF_TWS_report.pdf")

if textfile.exists():
    os.remove("/mnt/d/mail_project/result_TWS_Report.txt")
if pdffile.exists():
    os.remove("PDF_TWS_report.pdf")


my_file = open("/mnt/d/mail_project/result_TWS_Report.txt", "a+")
with open(filepath, 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if checkE in line:
            #print('string found in a file')
            #print('Line Number:', l_no)
            #print('Line:', line)
            print(line.strip())
            # don't look for next 
            
            my_file.writelines(line)
            

        if checkW in line:
            print(line.strip())
            
            my_file.writelines(line)
            
        if checkERR in line:
            print(line.strip())
            
            my_file.writelines(line)

my_file.close()
            


# save FPDF() class into 
# a variable pdf
pdf = FPDF()   
   
# Add a page
pdf.add_page()
   
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)

output_file = open("/mnt/d/mail_project/result_TWS_Report.txt", "r")

for pdf_line in output_file:
    #pdf.cell(200, 10, txt = pdf_line,border= 100, ln = 1, align = "L")
    #pdf.Cell(200, 10, txt = pdf_line, ln = 1, align = "L")
    pdf.multi_cell(200, 10, txt = pdf_line, align = "L")

pdf.output("PDF_TWS_report.pdf")

          
