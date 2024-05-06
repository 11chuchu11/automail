from docx.opc.exceptions import PackageNotFoundError
from docxtpl import DocxTemplate
from logger import ERROR, logging

def templateToDocx(template, docxName ,wordsToReplace={}):
  try:
    doc = DocxTemplate(f"{template}.docx")
    doc.render(wordsToReplace)
    doc.save(f"{docxName}.docx")
    return docxName
  except PackageNotFoundError as e:
    messageError=f"{ERROR} - Ocurrio un error en la lectura del archivo: {e}"
    print(messageError)
    logging.error(f"{messageError}: %s", e)
