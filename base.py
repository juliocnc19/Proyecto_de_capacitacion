from abc import ABC,abstractclassmethod

class Crud(ABC):
    nombre_archivo = None

    @abstractclassmethod
    def crear(cls,**kw):
        if 'identificador' in kw.keys():
            with open(cls.nombre_archivo,"r") as datos:
                listas = datos.readlines()
                for valor in listas:
                    row = valor.split("--")
                    if  kw.get('registro_a_guardar').split("--")[0] == row[0]:
                        #print("El identificador unico ya esta registrado")
                        return "El identificador unico ya esta registrado"
                        break
                else:
                    with open(cls.nombre_archivo,"a") as archivo:
                        archivo.write(kw.get('registro_a_guardar') + "\n")
                        #print("El registro fue registrado con exito")
                        return "El registro fue registrado con exito"
        else:
            with open(cls.nombre_archivo,"a") as archivo:
                        archivo.write(kw.get('registro_a_guardar') + "\n")
                        #print("El registro fue registrado con exito")
                        return "El registro fue registrado con exito"


    @abstractclassmethod
    def leer(cls):
        with open(cls.nombre_archivo,"r") as archivo:
            todos = archivo.readlines()
            return todos
            """print(f"\nREGISTROS GUARDADOS EN {kw.get('nombre_datos')}")
            for valor in kw.get('campos_persona'):
                print(valor)
            for elemento in todos:
                print(f"[{count}]==> {elemento}")
                count +=1"""

    @abstractclassmethod
    def eliminar(cls,**kw):
         with open(cls.nombre_archivo,"r") as archivo:
            lista_registros = archivo.readlines()
            for registro in lista_registros:
                row = registro.split("--")
                if kw.get('identificador') in row:
                    lista_registros.remove(registro)
                    with open(cls.nombre_archivo,"w") as nuevo:
                        nuevo.writelines(lista_registros)
                        print("Registro borrado con exito")
                        break
            else:
                print(kw.get('identificador'))

    @abstractclassmethod
    def actualizar(cls,**kw):
        with open(cls.nombre_archivo,"r") as archivo:
            datos = archivo.readlines()
            registro_a_cambiar = datos[kw.get('registro_a_cambiar')-1].split("--")
            registro_a_cambiar[kw.get('campo_a_cambiar')-1] = kw.get('nuevo_contenido')
            datos[kw.get('registro_a_cambiar')-1] = "--".join(registro_a_cambiar)

            for valor in datos:
                row = valor.split(",")
                if  kw.get('campo_a_cambiar') == 1 and kw.get('nuevo_contenido') == row[0]:
                    print("El identificador unico ya esta asociado a un registro")
                    break
            else:
                with open(cls.nombre_archivo,"w") as archivo:
                    archivo.writelines(datos)
                    print("El registro fue actualizado con exito")

    @abstractclassmethod
    def escribir_relacion(cls,**kw):
        with open(cls.nombre_archivo,"a") as archivo:
            archivo.write(kw.get("registro_a_guardar"))


class Persona(Crud):
    nombre_archivo = "persona.txt"
    pass

class Estudiante(Crud):
    nombre_archivo = "estudiante.txt"
    pass

class Salon(Crud):
    nombre_archivo = "salon.txt"
    pass

class Institucion(Crud):
    nombre_archivo = "institucion.txt"
    pass

class Relacion(Crud):
    nombre_archivo = "relacion.txt"
    pass
