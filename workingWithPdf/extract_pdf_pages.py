from PyPDF2 import PdfFileWriter, PdfFileReader


pdf_read = PdfFileReader('Pride_and_Prejudice.pdf')
pg_25 = pdf_read.getPage(25)

pdf_writer = PdfFileWriter()  # new instance if the writer class

# adding a blank pdf page to the write object, the parameters width and
# height are required as they determine the pages in points of height and width.
# one 1point is equal to 1/72 inches

# page = pdf_writer.addBlankPage(width=72, height=72)

# print(page)  # shows the page info

# adding item to pdf
# write the contents in binary write mode to the write method
# this will create a blank pdf file
# with open('my_pdf.pdf', 'wb') as output_file:
#     pdf_writer.write(output_file)


# extracting a page from the pdf reader and writing it to a new pdf

pdf_writer.addPage(pg_25)

# writing the contents to a new pdf file
with open('pg_25', 'wb') as prejudice:
    pdf_writer.write(prejudice)
