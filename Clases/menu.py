from Clase_Empleado import Empleado
from Clase_Tema import Tema

def eliminarEmpleado(self, idEmpleado): 
    with open('./archivos/Empleado.txt',"r+") as archivo: 
        nuevoArchivo= archivo.readlines()
        archivo.seek(0)
        for renglon in nuevoArchivo:
            if idEmpleado not in renglon: 
                archivo.write(renglon)
        archivo.truncate()

def eliminarTema(self, idTema):
    with open('./archivos/Tema.txt',"r+") as archivo:
        nuevoArchivo= archivo.readlines()
        archivo.seek(0)
        for renglon in nuevoArchivo:
            if idTema not in renglon:
                archivo.write(renglon)
        archivo.truncate()

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
            idEmpleado = int (input ("dame el id del empleado \n: "))
            nombre = input ("dame el nombre de tu empleado \n:")
            direccion = input ("ahora dame la direccion \n:")
            nuevoEmpleado = Empleado(idEmpleado, nombre, direccion)
            nuevoEmpleado.AgregarEmpleado(idEmpleado, nombre, direccion)
            print ("Tu empleado a sido agregado")
            print ("*" * 30 )
            print ("te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 2: 
            idABorrar = ("dime el id del empleado que deseas eliminar")
            eliminarEmpleado(idABorrar)
            print ("tu empleado a sido borrado")
            print ("*" * 30 )
            print ("te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 4: 
            print ("Se te mostrara toda la informacion en la base de datos ")
            archivo = open("./archivos/Empleado.txt",'r')
            print(archivo.read())
            archivo.close()
            print ("se te mostro la informacion requerida")
            print ("*" * 30 )
            final = int (input("te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )

        elif segundaOpcion == 5: 
            idRequerida = int(input("dime la id requerida del empleado que quieres ver"))
            mostrarEmpleadoEspecifico = Empleado(idRequerida)
            mostrarEmpleadoEspecifico.consultaEspecifica()
            print ("se te mostro el empleado")
            print ("*" * 30 )
            final = int (input("te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("te mostrare el menu inicial. \nElige una opcion" )
                opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:")) 
            elif final ==2: 
                print ("*" * 30 )
                print ("PROGRAMA TERMINADO")
                print ("*" * 30 )



if opcionInicial == 3:
    while opcionInicial == 3:
        print ("Elegiste Tema")
        print ("Este es el menu disponible: ")
        segundaOpcion = int(input("1. Agregar \n2. Borrar \n3. Modificar \n4. Ver Todo \n5. Ver Tema Especifico \n:"))
        if segundaOpcion == 1:
            print ("A continuacion te pedire algunos datos necesarios para agregar el tema: ")
            idTema = int(input("Dame el id del tema \n: "))
            nombre = input ("dame el nombre del tema \n: ")
            nuevoTema = Tema(idTema, nombre)
            nuevoTema.AgregarTema(idTema, nombre)
            print ("Tu tema se agrego")
            print ("*" * 30 )
            print ("te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 2:
            idAborrar = ("Dime el id del tema que deseas borrar")
            eliminarTema(idAborrar)
            print ("Tu tema se borro")
            print ("*" * 30 )
            print ("te mostrare el menu inicial. \nElige una opcion" )
            opcionInical = int(input("1. Empleado \n2. Curso \n3. Tema \n4. Video \n:"))

        elif segundaOpcion == 4:
            print ("Se te mostrara toda la informacion en la base de datos ")
            archivo = open("./archivos/Tema.txt",'r')
            print(archivo.read())
            archivo.close()
            print ("Se te mostro la informacion requerida")
            print ("*" * 30 )
            final = int (input("te gustaria continuar? 1. SI \n2. NO : "))
            if final == 1: 
                print ("te mostrare el menu inicial. \nElige una opcion" )
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


        

