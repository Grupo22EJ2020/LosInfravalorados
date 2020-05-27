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


    def consultaCurso (self):
        archivo = open ("./archivos/Cursos.txt",'r')
        for renglon in archivo:
            datosCurso = renglon.split ('|')
            print(f"Id: {datosCurso[0]} Nombre: {datosCurso[1]}")
        archivo.close()
    

     def consultaESPCurso (self,idCurso): 
        archivo = open('./archivos/Cursos.txt',"r",encoding='utf8')
        for renglon in archivo:
            print(f"No. Caracteres: {len(renglon)}: Renglon: {renglon}")
        archivo.close()    