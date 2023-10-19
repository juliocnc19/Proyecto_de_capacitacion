import flet as ft
from base import Salon,Institucion

class Crear(ft.UserControl):
    def arreglo_institucion(self):
            lista_institucion = []
            datos = Institucion.leer()
            for valor in datos:
                lista_institucion.append(ft.dropdown.Option(valor.split("--")[0] + " " + valor.split("--")[1].replace("\n","")))
            return lista_institucion

    def build(self):

        self.lista_institucion = []

        def guardar_institucion(e):
            if self.nombre_institucion.value == "" or self.codigo_institucion.value == "":
                self.mensaje.visible = True
            else:
                Institucion.crear(registro_a_guardar=f"{self.codigo_institucion.value}--{self.nombre_institucion.value}")
                self.nombre_institucion.value = ""
                self.codigo_institucion.value = ""
                self.institucion_a_elegir.options = self.arreglo_institucion()
                self.mensaje.visible = False
            self.update()

        def guardar_salon(e):
            if self.institucion_a_elegir.value == "" or self.numero_de_secciones.value == "":
                 self.mensaje_2.visible = True
            else:
                Salon.crear(registro_a_guardar=f"{self.institucion_a_elegir.value.split()[0]}--{self.numero_de_secciones.value}")
                self.institucion_a_elegir.value = ""
                self.numero_de_secciones.value = ""
                self.mensaje_2.visible = True
            self.update()

        self.numero_de_secciones = ft.Dropdown(
            label="Seccion",
            hint_text="Seleciona la seccion",
            options=[
                ft.dropdown.Option("1"),
                ft.dropdown.Option("2"),
                ft.dropdown.Option("3"),
                ft.dropdown.Option("4"),
                ft.dropdown.Option("5"),
                ft.dropdown.Option("6"),
                ft.dropdown.Option("7"),
                ft.dropdown.Option("8"),
                ft.dropdown.Option("9"),
                ft.dropdown.Option("10")
            ]
        )
        self.institucion_a_elegir = ft.Dropdown(
            label="Institucion",
            hint_text="Elige una institucion",
            options=self.arreglo_institucion()
        )

        self.nombre_institucion = ft.TextField(label="Nombre Institucion")
        self.codigo_institucion = ft.TextField(label="Codigo de la Institucion")
        self.mensaje = ft.Text("Ingrese los campos correctamente", visible=False)
        self.mensaje_2 = ft.Text("Ingrese los campos correctamente", visible=False)

        return ft.Row([
            ft.Column([
                ft.Text("Guardar Institucion"),
                ft.Container(
                    content = self.nombre_institucion,
                    margin = 20
                ),
                ft.Container(
                    content = self.codigo_institucion,
                    margin = 20
                ),
                ft.ElevatedButton(text="Guardar", on_click=guardar_institucion),
                self.mensaje
            ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column([
                ft.Text("Guardar Salon"),
                ft.Container(
                    content = self.institucion_a_elegir,
                    margin = 20
                ),
                ft.Container(
                    content = self.numero_de_secciones,
                    margin = 20
                ),
                ft.ElevatedButton(text="Guardar", on_click=guardar_salon)
            ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        )