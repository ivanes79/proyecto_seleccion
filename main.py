from config import *
from models import GetData,GetSalary,getemployees


empleadas_mujeres= getemployees('M')
print("empleadas mujer : ",empleadas_mujeres)
empleados_hombres= getemployees('H')
print("empleados hombre : ",empleados_hombres)
salario_bruto_anual=GetSalary()
print("Salario bruto anual : ",salario_bruto_anual,"€")


datos=GetData()
empleados=[]

for item in range(len(datos)):
    if datos[item][SALARIO_BRUTO] > '28000' and datos[item][ID_EMPRESA] == '2':
        
        empleados.append(datos[item])

for data in range(len(empleados)):
    print(empleados[data][ID_EMPLEADO],empleados[data][NOMBRE],empleados[data][APELLIDO1],empleados[data][APELLIDO2],empleados[data][SALARIO_BRUTO],empleados[data][EMPRESA])











