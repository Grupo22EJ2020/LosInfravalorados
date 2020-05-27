from Clase_Empleado import Empleado
from Clase_Tema import Tema
from Clase_Curso import Curso

def eliminarEmpleado(idEmpleado): 
    with open('./archivos/Empleado.txt',"r+") as archivo: 
        nuevoArchivo= archivo.readlines()
        archivo.seek(0)
        for renglon in nuevoArchivo:
            if idEmpleado not in renglon: 
                archivo.write(renglon)
        archivo.truncate()

def empleadoEspecifico (idEmpleado):
    archivo = open('./archivos/Empleado.txt',"r")
    for linea in archivo: 
        contenido = archivo.readlines(2)
        if contenido == idEmpleado: 
            print (linea) 

def eliminarTema(self, idTema):
    with open('./archivos/Tema.txt',"r+") as archivo:
        nuevoArchivo= archivo.readlines()
        archivo.seek(0)
        for renglon in nuevoArchivo:
            if idTema not in renglon:
                archivo.write(renglon)
        archivo.truncate()

def eliminarCurso(self,idCurso):
    with open('./archivos/Cursos.txt',"r+") as archivo:
        nuevoArchivo= archivo.readlines()
        archivo.seek(0)
        for renglon in nuevoArchivo:
            if idCurso not in renglon:
                archivo.write(renglon)
        archivo.truncate()


def eliminarCurso_Tema(self,idCurso_Tema):
    with open('./archivos/Curso_tema.txt',"r+") as archivo:
        nuevoArchivo= archivo.readlines()
        archivo.seek(0)
        for renglon in nuevoArchivo:
            if idCurso_Tema not in renglon:
                archivo.write(renglon)
        archivo.truncate()
def Curso_Tema_Especifico(idCurso_Tema):
    archivo = open('./archivos/Curso_tema.txt',"r")
    for linea in archivo: 
        contenido = archivo.readlines(2)
        if contenido == idCurso_Tema: 
            print (linea) 






print ("*"* 30)
print ("Te mostrare el menu inicial")
print ("Teclea el numero de la opcion donde deseas realizar un cambio")
opcionInicial =  int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n: "))

if opcionInicial == 1: 
    while opcionInicial == 1:
        print ("Elegiste EMPLEADOS") 
        print ("Este es el menu disponible: ")
        segundaOpcion = int(input("1. Agregar \n2. Borrar \n3. Modificar \n4. Ver Todo \n5. Ver Empleado Especifico \n:"))
        if segundaOpcion == 1: 
            print ("A continuacion de pedire algunos datos requeridos para agregar empleados:")
            idEmpleado = int (input ("Dame el id del empleado \n: "))
            nombre = input ("Dame el nombre de tu empleado \n:")
            direccion = input ("Ahora dame la direccion \n:")
            nuevoEmpleado = Empleado(idEmpleado, nombre, direccion)
            nuevoEmpleado.AgregarEmpleado(idEmpleado, nombre, direccion)
            print ("Tu empleado a sido agregado")
            print ("*" * 30 )
            print ("Te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 2: 
            idABorrar = input("Dime el id del empleado que deseas eliminar")
            eliminarEmpleado(idABorrar)
            print ("Tu empleado a sido borrado")
            print ("*" * 30 )
            print ("Te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 3: 
            idAModificar = input ("Dime el id del empleado que quieres modificar \n:")
            eliminarEmpleado(idAModificar)
            idEmpleado = int (input ("Dame el id \n: "))
            nombre = input ("Dame el onmbre \n:")
            direccion = input ("Dame la direccion \n:")
            empleadoModificado = Empleado(idEmpleado, nombre, direccion)
            empleadoModificado.AgregarEmpleado(idEmpleado, nombre, direccion)
        
        elif segundaOpcion == 4: 
            print ("Se te mostrara toda la informacion en la base de datos ")
            archivo = open("./archivos/Empleado.txt",'r')
            print(archivo.read())
            archivo.close()
            print ("SE TE MOSTRO LA INFORMACION REQUERIDA")
            print ("*" * 30 )
            final = int (input("Te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("Te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )

        elif segundaOpcion == 5: 
            idRequerida = input("Dime la id requerida del empleado que quieres ver")
            empleadoEspecifico(idRequerida)
            print ("SE TE MOSTRO EL EMPLEADO")
            print ("*" * 30 )
            final = int (input("Te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("Te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )
elif opcionInicial == 3:
    while opcionInicial == 3:
        print ("Elegiste Tema")
        print ("Este es el menu disponible: ")
        segundaOpcion = int(input("1. Agregar \n2. Borrar \n3. Modificar \n4. Ver Todo \n5. Ver Tema Especifico \n:"))
        if segundaOpcion == 1:
            print ("A continuacion te pedire algunos datos necesarios para agregar el tema: ")
            idTema = int(input("Dame el id del tema \n: "))
            nombre = input ("Dame el nombre del tema \n: ")
            nuevoTema = Tema(idTema, nombre)
            nuevoTema.AgregarTema(idTema, nombre)
            print ("Tu tema se agrego")
            print ("*" * 30 )
            print ("Te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 2:
            idAborrar = ("Dime el id del tema que deseas borrar")
            eliminarTema(idAborrar)
            print ("Tu tema se borro")
            print ("*" * 30 )
            print ("Te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 4:
            print ("Se te mostrara toda la informacion en la base de datos ")
            archivo = open("./archivos/Tema.txt",'r')
            print(archivo.read())
            archivo.close()
            print ("Se te mostro la informacion requerida")
            print ("*" * 30 )
            final = int (input("Te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("Te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )

        elif segundaOpcion == 5:
            idRequerida = int(input("Dime el id requerida del tema que quieres ver"))
            mostrarTemaEspecifico = Tema(idRequerida)
            mostrarTemaEspecifico.consultaEspecifica()
            print ("Se te mostro el empleado")
            print ("*" * 30 )
            final = int (input("te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )

elif opcionInicial == 2: 
    while opcionInicial == 2:
        print ("Elegiste CURSOS") 
        print ("Este es el menu disponible: ")
        segundaOpcion = int(input("1. Agregar \n2. Borrar \n3. Modificar \n4. Ver Todo \n5. Ver Curso Especifico \n6. Ver Union Curso-Tema \n7. Ver union Curso-Video")
        if segundaOpcion == 1:    
            print ("A continuacion de pedire algunos datos requeridos para agregar Cursos:")
            idCurso = int (input ("Dame el id del curso \n: "))
            descripcion = input ("Dame la descripcion del curso \n:")
            idEmpleado = input ("Dame la id del empleado \n:")
            nuevoCurso = Curso(idCurso, descripcion, idEmpleado)
            nuevoCurso.AgregarCurso(idCurso, descripcion, idEmpleado)
            print ("Tu curso a sido agregado")
            print ("*" * 30 )
            print ("Te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))
        elif segundaOpcion == 2: 
            idABorrar = input("Dime el id del curso que deseas eliminar")
            eliminarCurso(idABorrar)
            print ("Tu curso a sido borrado")
            print ("*" * 30 )
            print ("Te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))
        elif segundaOpcion == 3: 
            idAModificar = input ("Dime el id del curso que quieres modificar \n:")
            eliminarCurso(idAModificar)
            idCurso = int (input ("Dame el id del curso \n: "))
            descripcion = input ("Dame la descripcion del curso\n:")
            idEmpleado = input ("Dame la id del empleado \n:")
            cursoModificado = Curso(idCurso, descripcion, idEmpleado)
            cursoModificado.AgregarCurso(idCurso, descripcion, idEmpleado)
        elif segundaOpcion == 4: 
            print ("Se te mostrara toda la informacion en la base de datos ")
            archivo = open("./archivos/Cursos.txt",'r')
            print(archivo.read())
            archivo.close()
            print ("SE TE MOSTRO LA INFORMACION REQUERIDA")
            print ("*" * 30 )
            final = int (input("Te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("Te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )
        elif segundaOpcion == 5: 
            idRequerida = input("Dime la id requerida del curso que quieres ver")
            consultaESPCurso(idRequerida)
            print ("SE TE MOSTRO EL CURSO")
            print ("*" * 30 )
            final = int (input("Te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("Te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )
        elif segundaOpcion == 6: 
            terceraOpcion = int(input("que quieres hacer con la union Curso-Tema? 1. Agregar \n2. Borrar \n3. Modificar \n4. Ver Todo \n5. Ver Curso-Tema Especifico") 
            if terceraOpcion == 1: 
                idCurso_Tema = int (input ("Dame el id del Curso-Tema \n: "))
                idTema =  input ("Dame el id del tema\n:")
                idCurso = input ("Dame la id del curso \n:")
                nuevoCurso_Tema = Curso_Tema(idCurso_Tema, idCurso, idTema)
                nuevoCurso_Tema.AgregarVinculo(idCurso_Tema, idCurso, idTema)
                print ("Tu vinculo a sido agregado")
                print ("*" * 30 )
                print ("Te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

            

