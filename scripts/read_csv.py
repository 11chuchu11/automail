#!LECTURA DEL CSV
import csv


def readCsv(csvFile):
    data=[]
    with open(f"{csvFile}.csv", 'r',newline='') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            # to = row[0]
            # subject = row[1]
            # body = row[2].replace(r"\n", "\n") if len(row) >= 3 else ''
            # namePerson = row[3]
            # attached = row[4:] if len(row) >= 5 else []
            # body = body.replace("#persona#", namePerson)
            data.append(row[0])
    return data