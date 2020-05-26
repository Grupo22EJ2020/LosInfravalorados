class Empleado() :
     def __init__(self, idEmpleado, nombre, direccion): 
         self.idEmpleado = idEmpleado 
         self.nombre = nombre 
         self.direccion = direccion


     def AgregarEmpleado (self,idEmpleado,nombre,direccion): 
         archivo = open("./archivos/Empleado.txt",'a')
         numeroInt= str (idEmpleado)
         archivo.write (numeroInt + "|" + nombre + "|" + direccion )

         archivo.close()


     def consultaEspecifica (self, idEmpleado): 
         archivo = open('./archivos/Empleado.txt',"r",encoding='utf8')
         for renglon in archivo:
             print(f"No. Caracteres: {len(renglon)}: Renglon: {renglon}")
         archivo.close()

         
     
        



