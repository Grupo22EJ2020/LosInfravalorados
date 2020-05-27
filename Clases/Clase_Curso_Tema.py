class Curso_Tema(): 
     def __init__(self,idCursoTema,idCurso, idTema): 
        self.idCursoTema = idCursoTema 
        self.idCurso = idCurso
        self.idTema = idTema 

     def AgregarVinculo (self,idCursoTema, idCurso, idTema): 
         archivo = open("./archivos/Empleado.txt",'a')
         numeroInt= str (idCursoTema)
         archivo.write (numeroInt + "|" + idCurso + "|" + idTema + "|" + '\n')
         archivo.close()
    

        

