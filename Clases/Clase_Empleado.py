class Empleado() :
     def __init__(self, idEmpleado, nombre, direccion): 
         self.idEmpleado = idEmpleado 
         self.nombre = nombre 
         self.direccion = direccion


    def agregarEmpleado (self, idEmpleado, nombre, direccion):
         print (30 * "*")
         archivo = open("./archivos/Empleado.txt",'a')
         archivo.write (idEmpleado)
         archivo = open("./archivos/Empleado.txt",'a')
         archivo.write (nombre)
         archivo = open("./archivos/Empleado.txt",'a')
         archivo.write (direccion)
         archvios.close()
        

