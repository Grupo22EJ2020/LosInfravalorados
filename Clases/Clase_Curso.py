class Curso() :
     def __init__(self, idCurso, descripcion, idEmpleado): 
         self.idCurso = idCurso 
         self.descripcion = descripcion 
         self.idEmpleado = idEmpleado
         

     def AgregarCurso(self, idCurso, descripcion, idEmpleado): 
         archivo = open("./archivos/Curso.txt",'a')
         numeroInt= str (idCurso)
         archivo.write (numeroInt + "|" + descripcion + "|" + idEmpleado + "|" "\n")
         archivo.close()