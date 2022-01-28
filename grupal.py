from typing import Match

opcion=0
def menu():
    opc= int(input( "MENU PRINCIPAL            \n " +  
                   "1.- CARGO   \n " +
                   "2.-DEPARTAMENTO   \n " +
                   "3.- EMPLEADOS  \n " +
                   "4.- SALIR  \n " +               
                    "ELIJA UNA OPCION: "))
    return opc 
while opcion !=6:
    opcion = menu ()
    if opcion==1 :
        while True:    
            print("MANTENIMIENTO DE CARGOS ")
            print("1.- INGRESO ")
            print("2.- CONSULTA") 
            print("3.- SALIR ")
            opcion=int(input("Accion a ejecutar:  "))
            if opcion==1:
                print
        
    elif opcion==2:
           men=0
           while True:      
                print(" MANTENIMIENTO DE DEPARTAMENTOS")
                print("1).-  INGRESO ")
                print("2).-  CONSULTA  ") 
                print("3).-   SALIR   ")
                men=int(input("ACCION A EJECUTAR:  "))
                if men==1: 
                      print(" INGRESO DE DEPARTAMENTOS")
                      departamento = int(input("INGRESE A QUE DEPARTAMENTO PERTENECE: "))
                      class Departamento:
                          
                          secuencia=0
                          departamentos = []
                          def _init_(self, descrip):
                             self.codigo =descrip
                             self.departamento = descrip
                          def  registro(self):
                              return 
                           
                elif men ==2:
                    print("LISTADO DE DEPARTAMENTOS ")
                    
                
                elif men==3:
                    print("SALIO DE LA OPCION DE MANTENIMIENTO DE EMPLEADOS")
                
    elif opcion==3:
           men=0
           while True:      
                print(" MANTENIMIENTO  DE EMPLEADOS ")
                print("1).-  INGRESO ")
                print("2).-  CONSULTA  ") 
                print("3).-   SALIR   ")
                men=int(input("ACCION A EJECUTAR:  "))
                if men==1: 
                    codigo=0
                    nombre= int (input("INGRESE SU NOMBRE:    "))
                    cedula= int (input("INGRESE SJ NUMERO DE CEDULA:   "))
                    cargo= int (input("INGRESE SU CARGO :   "))
                    departamento= int (input("INGRESE A QUE DEPARTAMENTO PERTENESE:   "))
                    sueldo= int (input("INGRESE SU SUELDO:     "))
                    class Empleado:
                        secuencia=0
                        Empleados=( “codigo”:1,”nombre”:”Dan”,”cedula”:”0914192182”,”cargo”:1,”departamento”;1,”sueldo”:500.50)
                    def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo  )  
                             self.codigo = codigo 
                             self.nombre = nombre
                             self.cedula= cedula
                             self.cargo = codCargo
                             self.departamento = codDepartamento
                             self.sueldo = sueldo
                    def  registro(self):
                                 return [{}….]
