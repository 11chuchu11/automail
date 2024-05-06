from read_json import readJson 
from read_csv import readCsv
import json as js
jsonFileName= 'ejemplo'#input('Nombre del archivo json: ')
csvFileName = 'listacorreos'#input('Nombre del archivo csv: ')
data = readJson(jsonFileName)
emailsArr = readCsv(csvFileName)

json = {}
json['emailemisor'] = data['emailemisor']
json['password'] = data['password']
json['receptores']=[]

for email in emailsArr:
    
    emailDict={}
    emailDict['email']=email
    emailDict['asunto']=data['ejemplo']['asunto']
    emailDict['cuerpo']=data['ejemplo']['cuerpo']
    emailDict['remplazos']=data['ejemplo']['remplazos']
    emailDict['archivos']=data['ejemplo']['archivos']
    emailDict['templates']=data['ejemplo']['templates']
    
    json['receptores'].append(emailDict)
    
    

fileName= input('Nombre del archivo json: ')

with open(f"{fileName}.json",'w',encoding="utf-8") as file:
    js.dump(json, file, ensure_ascii=False)
print(f"Archivo JSON '{fileName}' creado correctamente.")