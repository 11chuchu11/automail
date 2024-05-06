from docx2pdf import convert

def docxToPdf(filename):
    convert(f"{filename}.docx")
    
    return f"{filename}.pdf"


