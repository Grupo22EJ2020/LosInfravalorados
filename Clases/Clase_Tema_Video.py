class Curso_Tema_Video(): 
     def __init__(self,idCursoTemaVideo,idCurso_Tema, idVideo): 
        self.idCursoTema = idCursoTema_Video 
        self.idCurso = idCurso_Tema
        self.idTema = idVideo

     def AgregarVinculoCTV (self,idCursoTema_Video, idCurso_Tema, idVideo): 
         archivo = open("./archivos/Curso_Tema_Video.txt",'a')
         numeroInt= str (idCursoTema_Video)
         archivo.write (numeroInt + "|" + idCurso_Tema + "|" + idVideo + "|" + '\n')
         archivo.close()
        