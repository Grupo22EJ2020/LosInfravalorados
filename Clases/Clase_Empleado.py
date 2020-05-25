class Empleado() :
     def __init__(self, idEmpleado, nombre, direccion): 
         self.idEmpleado = idEmpleado 
         self.nombre = nombre 
         self.direccion = direccion


     def AgregarEmpleado (self,idEmpleado,nombre,direccion): 
         archivo = open("./archivos/Empleado.txt",'a')
         numeroInt= str (self.idEmpleado)
         archivo.write (numeroInt)
         archivo.write (self.nombre)
         archivo.write (self.direccion)
         archivo.close()
    
     def consultaCompleta (self): 
         archivo = open ("./archivos/Empleado.txt",'r')
         for renglon in archivo: 
             datosEmpleados = renglon.split('|')
             print (f'Id: {datosEmpleados[0]} Nombre: {datosEmpleados[1]} Direccion: {datosEmpleados[2]}')
         archivo.close() 

     def consultaEspecifica (self, idEmpleado): 
         archivo = open('./archivos/Empleado.txt',"r",encoding='utf8')
         for renglon in archivo:
             print(f"No. Caracteres: {len(renglon)}: Renglon: {renglon}")
         archivo.close()
    


