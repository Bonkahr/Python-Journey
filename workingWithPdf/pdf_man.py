from PyPDF2 import PdfFileReader

pdf = PdfFileReader('edna.pdf')

print(pdf.getNumPages())
pdf_info = pdf.documentInfo
print(pdf_info.title)

first_page = pdf.getPage(0)     # returns a page object

# extracting texts from the page
first_page_texts = first_page.extractText()

# printing the texts
print(first_page_texts, end="")

# looping through all the pages of the pdf and copying them in a text file

with open('edna.txt', 'w') as my_file:
    my_file.write(
        f'{pdf.documentInfo.title}\n'
        f'Number of pages: {pdf.getNumPages()}\n\n'
    )

    for page in pdf.pages:
        text = page.extractText()
        my_file.write(text)
