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

    def consultaTema (self):
        archivo = open ("./archivos/Tema.txt",'r')
        for renglon in archivo:
            datosTema = renglon.split ('|')
            print(f"Id: {datosTema[0]} Nombre: {datosTema[1]}")
        archivo.close()

    def consultaEspTema (self,idTema):
        archivo = open ("./archivos/Tema.txt",'r',encoding='utf8')
        for renglon in archivo:
            print(f"No. Caracteres:{len(renglon)}: Renglon: {renglon} ")
        archivo.close()
        
    
