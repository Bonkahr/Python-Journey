import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

# Display file selection dialogue for opening a pdf file

input_path = gui.fileopenbox(
    title='Select a PDF file to rotate... ',
    default='*.pdf'
)

# Exit the program if the user closed the window without choosing a file

if input_path is None:
    exit()

# Ask the user the angle to rotate the file

choices = ['90', '180', '270']
degrees = int(gui.buttonbox(
    msg='Rotate the PDF clockwise at which angle?',
    title='Chose rotation angle....',
    choices=choices,
))

# Get the output file path from the user to save file
output_path = gui.filesavebox(
    title='Save the rotated file as ....',
    default='*.pdf'
)

# User doesn't use the same file name in the same directory
while input_path == output_path:
    # Alert the user
    gui.msgbox(msg='You are about to overwrite the original file, Not allowed')
    output_path = gui.filesavebox(
        title='Save the rotated file as ....',
        default='*.pdf'
    )

# if user cancels without saving the program exits
if output_path is None:
    exit()

# Rotating the PDF file
input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

for page in input_file.pages:
    page = page.rotateClockwise(degrees)
    output_pdf.addPage(page)

# Saving the Rotated files

with open(output_path, 'wb') as output_file:
    output_pdf.write(output_file)
