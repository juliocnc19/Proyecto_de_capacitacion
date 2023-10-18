import flet as ft
from base import Persona,Estudiante,Salon,Institucion,Relacion

class Analista(ft.UserControl):
    #funcion que costruye todo el control de usuario
    def arreglo_institucion(e):
        datos = Institucion.leer()
        lista_institucion = []
        for valor in datos:
            lista_institucion.append(ft.dropdown.Option(valor.split("--")[0] + " " + valor.split("--")[1].replace("\n","")))
        return lista_institucion
    
    def build(self):
        self.lista_salon = []
        self.tabla_relacion = []

        def obtener_relacion(e):
            self.tabla_relacion.clear()
            datos_relacion = Relacion.leer()
            for datos in datos_relacion:
                valor = datos.split("--")
                self.tabla_relacion.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(valor[0])),
                        ft.DataCell(ft.Text(valor[1])),
                        ft.DataCell(ft.Text(valor[2])),
                        ft.DataCell(ft.Text(valor[3])),
                        ft.DataCell(ft.Text(valor[4])),
                        ft.DataCell(ft.Text(valor[5].replace("\n",""))),
                    ]
                ))
            self.update()

        def arreglo_salon(e):
            self.lista_salon.clear()
            datos_salon = Salon.leer()
            for valor_salon in datos_salon:
                valor = valor_salon.split("--")[0]
                institucion = self.institucion.value.split()[0]
                if valor == institucion:
                    self.lista_salon.append(ft.dropdown.Option("Seccion: " + valor_salon.split("--")[1].replace("\n","")))
                
            self.update()
            
        def actualizar_institucion(e):
            self.institucion.options = self.arreglo_institucion()
            self.update()

        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Cedula")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Edad"), numeric=True),
                ft.DataColumn(ft.Text("Grado")),
                ft.DataColumn(ft.Text("Seccion")),
                ft.DataColumn(ft.Text("Intitucino")),
            ],
            rows=self.tabla_relacion,
        )

        self.grado = ft.Dropdown(
            on_change = actualizar_institucion,
            label = "Grado",
            hint_text="Seleciona el grado",
            options = [
                ft.dropdown.Option("1"),
                ft.dropdown.Option("2"),
                ft.dropdown.Option("3"),
                ft.dropdown.Option("4"),
                ft.dropdown.Option("5"),
                ft.dropdown.Option("6"),
                ft.dropdown.Option("7")
            ]
        )
        self.institucion = ft.Dropdown(
            on_change = arreglo_salon,
            label="Institucion",
            hint_text="Eligue la Institucion",
            options= self.arreglo_institucion()
        )
        self.salon = ft.Dropdown(
            label="Salon",
            hint_text="Eligue el Salon",
            options= self.lista_salon
        )
        
        self.nombre = ft.TextField(label="Nombre", autofocus=True, on_change=actualizar_institucion)
        self.cedula = ft.TextField(label="Cedula")
        self.edad = ft.TextField(label="edad")
        self.boton = ft.ElevatedButton(text="Registrar")

        #funcion que se encarga de llamar a la clase para crear el registro
        def crear_registro(e):
            Persona.crear(registro_a_guardar=f"{self.cedula.value}--{self.nombre.value}--{self.edad.value}")
            Estudiante.crear(registro_a_guardar=f"{self.cedula.value}--{self.grado.value}--{self.salon.value.split()[1]}")
            Relacion.escribir_relacion(registro_a_guardar=f"{self.cedula.value}--{self.nombre.value}--{self.edad.value}--{self.grado.value}--{self.salon.value.split()[1]}--{self.institucion.value}\n")
            self.nombre.value = ""
            self.cedula.value = ""
            self.edad.value = ""
            self.grado.value = ""
            self.institucion.value = ""
            self.salon.value = ""
            self.update()
        #AQUI TODOS LOS ELEMENTOS QUE SE VAN A MOSTRAR
        return ft.Row([
            ft.Column([
                ft.Container(
                    content = self.nombre,
                    margin = 10
                ),
                ft.Container(
                    content = self.cedula,
                    margin = 10
                ),
                ft.Container(
                    content = self.edad,
                    margin = 10
                ),
                ft.Container(
                    content = self.grado,
                    margin = 10
                ),
                ft.Container(
                    content = self.institucion,
                    margin = 10
                ),
                ft.Container(
                    content = self.salon,
                    margin = 10
                ),
                ft.ElevatedButton(text="Registrar", on_click=crear_registro,on_hover=obtener_relacion)

            ]),
            ft.Container(
                on_hover=obtener_relacion,
                content=self.tabla,
                alignment=ft.alignment.top_right,
                margin = 10
            )
        ])
