class Tema():
    def __init__(self,idTema,nombre):
        self.idTema = idTema
        self.nombre = nombre

    def AgregarTema(self,idTema,nombre):
        archivo = open("./archivos/Tema.txt",'a')
        idTema = int(input("Ingresa el numero asignado al tema: "))
        nombre = input("Ingresa el nombre del tema: ")
        archivo.write(idTema + "|"+ nombre + "|" + idTema + "|" + "\n")
        archivo.close()

    
        
    
