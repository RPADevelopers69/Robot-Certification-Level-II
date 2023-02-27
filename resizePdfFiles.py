import os
import PyPDF2

# Define a function to resize a single PDF file
def resize_pdf_file(input_path, output_path):
    # Open the PDF file in read binary mode
    with open(input_path, 'rb') as input_file:
        # Create a PyPDF2 PdfFileReader object from the input file
        pdf_reader = PyPDF2.PdfFileReader(input_file)
        # Create a PyPDF2 PdfFileWriter object to write the output file
        pdf_writer = PyPDF2.PdfFileWriter()
        # Loop through all the pages in the input file
        for page_number in range(pdf_reader.getNumPages()):
            # Get the current page from the input file
            page = pdf_reader.getPage(page_number)
            # Scale the page by a factor of 1.5 (both horizontally and vertically)
            page.scale(1.5, 1.5)
            # Add the scaled page to the output file
            pdf_writer.addPage(page)
        # Open the output file in write binary mode
        with open(output_path, 'wb') as output_file:
            # Write the contents of the output PDF writer to the output file
            pdf_writer.write(output_file)

# Define the input and output directories
input_directory = ''
output_directory = ''

# Loop through all the PDF files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.pdf'):
        # Get the full path to the input file
        input_path = os.path.join(input_directory, filename)
        # Get the full path to the output file
        output_path = os.path.join(output_directory, filename)
        # Resize the PDF file
        resize_pdf_file(input_path, output_path)
