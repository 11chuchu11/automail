from logger import logging, ERROR
import os
from docx_to_pdf import docxToPdf
from generate_docx import templateToDocx
from read_json import readJson
from send_email import sendMail

jsonFileName=input("Como se llama el listado a enviar?: ")


try:
  jsonData=readJson(jsonFileName)
  filesFromTemplates=[]

  myEmail=jsonData["emailSender"]
  password=jsonData["password"]
  receivers = jsonData["receivers"]

  if __name__ == "__main__":
    
      for receiver in receivers:
        try:
          email=receiver["email"]
          print(f"Enviando email a {email}")
          asunto=receiver["subject"]
          cuerpo=receiver["body"]
          remplazos=receiver["replacements"]
          archivos=[]
          templates=receiver["templates"]
          if len(receiver['files'])>0:
            for file in receiver['files']:
              archivos.append(file['path'])

          if len(templates)>0:
            for template in templates:
              print(template)
              templateName=template["template"]['name']
              generatedFileName=template["name"]
              print(f"Generando docx {generatedFileName}")
              nameDocx = templateToDocx(f"{templateName}",generatedFileName,remplazos)
              print(f"Convirtiendo {generatedFileName} a pdf")
              namePdf=docxToPdf(nameDocx)
              archivos.append(namePdf)
              filesFromTemplates.clear()
              filesFromTemplates.append(namePdf)
              filesFromTemplates.append(f"{nameDocx}.docx")

          for key in remplazos:
            cuerpo=cuerpo.replace(f"###{key}###", remplazos[key])


          sendMail(myEmail, password,email, asunto, cuerpo, archivos)
          print("Email enviado")
        except FileNotFoundError as e:
          messageError=f"{ERROR} - Ocurrio un error en la lectura de archivo"
          print(f"{messageError}: {e}")
          logging.error(f"{messageError}: %s", e)
        except KeyError as e:
          messageError=f"{ERROR} - clave incongruente"
          print(f"{messageError}: {e}")
          logging.error(f"{messageError}: %s", e)
        finally:
          if len(templates)>0:
            for file in filesFromTemplates:
              os.remove(file)
except FileNotFoundError as e:
  messageError=f"{ERROR} - Ocurrio un error en la lectura de archivo"
  print(f"{messageError}: {e}")
  logging.error(f"{messageError}: %s", e)
except Exception as e:
  logging.error("Ocurrio un Error: %s", e)
  print("Ocurrio un error ", e)

