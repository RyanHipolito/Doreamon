import PyPDF2

if file is not None:
    # Read the PDF file
    pdf_reader = PyPDF2.PdfFileReader(file)
    # Extract the content
    content = ""
    for page in range(pdf_reader.getNumPages()):
        content += pdf_reader.getPage(page).extractText()
    # Display the content
    st.write(content)
