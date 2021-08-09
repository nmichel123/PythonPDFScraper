import PyPDF2

FILE_PATH =  'pdf.pdf'

with open(FILE_PATH, mode='rb') as f:

    reader = PyPDF2.PdfFileReader(f)

    page = reader.getPage(0)

    print(page.extractText())

    writer = PyPDF2.PdfFileWriter()

    writer.appendPagesFromReader(reader,after_page_append=None)

    with open ('newdoc.pdf', 'wb') as doc:
        writer.write(doc)
