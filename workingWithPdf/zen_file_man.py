from PyPDF2 import PdfFileReader

pdf = PdfFileReader('zen.pdf')
print(pdf.getNumPages())

# printing the first page of the file to a zen.txt file

with open('zen.txt', 'w') as zen:
    zen.write(pdf.getPage(0).extractText())
