from PyPDF2 import PdfFileReader, PdfFileWriter


my_pdf = PdfFileReader('Pride_and_Prejudice.pdf')

pdf_write = PdfFileWriter()

# for page in range(1, 4):
#     pages = my_pdf.getPage(page)
#     pdf_write.addPage(pages)

# instead of the range gen loop above, you can use the slice method to loop
# through the pages using the pages method

for page in my_pdf.pages[1:4]:
    pdf_write.addPage(page)

with open('my_pride_ch1.pdf', 'wb') as file:
    pdf_write.write(file)

