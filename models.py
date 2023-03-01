import csv
from config import *


def GetData():
    fichero = open(DATA_EMPLEADOS,"r")
    csvReader = csv.reader(fichero,delimiter=";",quotechar='"')
    datos=[]
    for item in csvReader:
        datos.append(item)
    fichero.close()
    return datos


def GetSalary():
    salario_bruto_anual=0
    datos=GetData()
    for item in range(len(datos)):
        if datos[item][ID_EMPRESA] == '1' or datos[item][ID_CENTRO_DE_TRABAJO] == 'CT2':
            salario_bruto_anual += int(datos[item][SALARIO_BRUTO])

    return salario_bruto_anual

def getemployees(S):
    empleados=0
    datos=GetData()
    for item in range(len(datos)):
        if datos[item][SEXO] == S:
            empleados += 1
            
    return empleados

