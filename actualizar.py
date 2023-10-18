import flet as ft
from base import Persona,Estudiante,Salon,Institucion,Relacion

class Actualizar(ft.UserControl):
    

    def build(self):
        ######################
        self.datos_persona = []
        self.datos_estudiante = []
        self.datos_salon = []
        self.datos_institucion = []
        ############################
        def datos_persona(e):
            self.datos_persona.clear()
            datos_persona = Persona.leer()
            count = 1
            for datos in datos_persona:
                valor = datos.split("--")
                self.datos_persona.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(count)),
                        ft.DataCell(ft.Text(valor[0])),
                        ft.DataCell(ft.Text(valor[1])),
                        ft.DataCell(ft.Text(valor[2].replace("\n",""))),
                    ],
                ))
                count += 1
            self.update()

        self.tabla_personas = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nº Registro")),
                ft.DataColumn(ft.Text("Cedula")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Edad"), numeric=True)
            ],
            rows=self.datos_persona,
        )
        self.elegir_registro_persona = ft.TextField(label="Registro a cambiar",hint_text="Digite el numero de registro")
        self.elegir_campo_persona = ft.Dropdown(
            label="Campo",
            hint_text="Eligue un campo",
            options=[
                ft.dropdown.Option(text="Cedula"),
                ft.dropdown.Option(text="Nombre"),
                ft.dropdown.Option(text="Edad"),
            ]
        )
        self.nuevo_contenido_persona = ft.TextField(label="Nuevo Contenido",hint_text="Nuevo contenido")

        #################################
        def datos_estudiante(e):
            self.datos_estudiante.clear()
            datos_estudiante = Estudiante.leer()
            count = 1
            for datos in datos_estudiante:
                valor = datos.split("--")
                self.datos_estudiante.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(count)),
                        ft.DataCell(ft.Text(valor[0])),
                        ft.DataCell(ft.Text(valor[1])),
                        ft.DataCell(ft.Text(valor[2].replace("\n",""))),
                    ],
                ))
                count += 1
            self.update()

        self.tabla_estudiantes = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nº Registro")),
                ft.DataColumn(ft.Text("Cedula")),
                ft.DataColumn(ft.Text("Grado")),
                ft.DataColumn(ft.Text("Seccion"), numeric=True)
            ],
            rows=self.datos_estudiante,
        )
        self.elegir_registro_estudiante = ft.TextField(label="Registro a cambiar",hint_text="Digite el numero de registro")
        self.elegir_campo_estudiante = ft.Dropdown(
            label="Campo",
            hint_text="Eligue un campo",
            options=[
                ft.dropdown.Option(text="Cedula"),
                ft.dropdown.Option(text="Grado"),
                ft.dropdown.Option(text="Seccion"),
            ]
        )
        self.nuevo_contenido_estudiante = ft.TextField(label="Nuevo Contenido",hint_text="Nuevo contenido")

        ###################################################################################

        def datos_salon(e):
            self.datos_salon.clear()
            datos_salon = Salon.leer()
            count = 1
            for datos in datos_salon:
                valor = datos.split("--")
                self.datos_salon.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(count)),
                        ft.DataCell(ft.Text(valor[0])),
                        ft.DataCell(ft.Text(valor[1].replace("\n","")))
                    ],
                ))
                count += 1
            self.update()

        self.tabla_salon = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nº Registro")),
                ft.DataColumn(ft.Text("ID_Salon")),
                ft.DataColumn(ft.Text("Seccion")),
            ],
            rows=self.datos_salon,
        )
        self.elegir_registro_salon = ft.TextField(label="Registro a cambiar",hint_text="Digite el numero de registro")
        self.elegir_campo_salon= ft.Dropdown(
            label="Campo",
            hint_text="Eligue un campo",
            options=[
                ft.dropdown.Option(text="ID_Salon"),
                ft.dropdown.Option(text="Seccion"),
            ]
        )
        self.nuevo_contenido_salon = ft.TextField(label="Nuevo Contenido",hint_text="Nuevo contenido")

        ####################################################################################################

        def datos_institucion(e):
            self.datos_institucion.clear()
            datos_institucion = Institucion.leer()
            count = 1
            for datos in datos_institucion:
                valor = datos.split("--")
                self.datos_institucion.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(count)),
                        ft.DataCell(ft.Text(valor[0])),
                        ft.DataCell(ft.Text(valor[1].replace("\n",""))),
                    ],
                ))
                count += 1
            self.update()

        self.tabla_institucion = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nº Registro")),
                ft.DataColumn(ft.Text("ID_Institucion")),
                ft.DataColumn(ft.Text("Nombre")),
            ],
            rows=self.datos_institucion,
        )
        self.elegir_registro_institucion = ft.TextField(label="Registro a cambiar",hint_text="Digite el numero de registro")
        self.elegir_campo_institucion = ft.Dropdown(
            label="Campo",
            hint_text="Eligue un campo",
            options=[
                ft.dropdown.Option(text="ID_Institucion"),
                ft.dropdown.Option(text="Nombre"),
            ]
        )
        self.nuevo_contenido_institucion = ft.TextField(label="Nuevo Contenido",hint_text="Nuevo contenido")

        ###################################################################################################3

        def actualizar_personas(e):
            campo = ""
            if self.elegir_campo_persona.value == "Cedula":
                campo = 1
                Estudiante.actualizar(registro_a_cambiar=int(self.elegir_registro_persona.value),campo_a_cambiar=campo,nuevo_contenido=self.nuevo_contenido_persona.value)
                Relacion.actualizar(registro_a_cambiar=int(self.elegir_registro_persona.value),campo_a_cambiar=campo,nuevo_contenido=self.nuevo_contenido_persona.value)
            elif self.elegir_campo_persona.value == "Nombre":
                campo = 2
                Relacion.actualizar(registro_a_cambiar=int(self.elegir_registro_persona.value),campo_a_cambiar=campo,nuevo_contenido=self.nuevo_contenido_persona.value)
            elif self.elegir_campo_persona.value == "Edad":
                campo = 3
                Persona.actualizar(registro_a_cambiar=int(self.elegir_registro_persona.value),campo_a_cambiar=campo,nuevo_contenido=f"{self.nuevo_contenido_persona}\n")
                Relacion.actualizar(registro_a_cambiar=int(self.elegir_registro_persona.value),campo_a_cambiar=campo,nuevo_contenido=str(self.nuevo_contenido_persona.value))
            Persona.actualizar(registro_a_cambiar=int(self.elegir_registro_persona.value),campo_a_cambiar=campo,nuevo_contenido=str(self.nuevo_contenido_persona.value))
            self.elegir_campo_estudiante.value = ""
            self.elegir_registro_persona.value = ""
            self.nuevo_contenido_persona.value = ""
            self.update()
            

        #########################################################################################################
        ######################################################################################################

        return ft.Column([
            ft.Row([
                ft.Container(
                    content=self.tabla_personas,
                    on_hover=datos_persona
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Personas", size=30),
                        self.elegir_registro_persona,
                        self.elegir_campo_persona,
                        self.nuevo_contenido_persona,
                        ft.ElevatedButton(text="Actualizar", on_click=actualizar_personas, on_hover=datos_persona)
                    ])
                )
            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            ############################################
            ft.Row([
                ft.Container(
                    content=self.tabla_estudiantes,
                    on_hover=datos_estudiante
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Estudiantes", size=30),
                        self.elegir_registro_estudiante,
                        self.elegir_campo_estudiante,
                        self.nuevo_contenido_estudiante,
                        ft.ElevatedButton(text="Actualizar")
                    ])
                )
            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            ############################################
            ft.Row([
                ft.Container(
                    content=self.tabla_salon,
                    on_hover=datos_salon
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Salon", size=30),
                        self.elegir_registro_salon,
                        self.elegir_campo_salon,
                        self.nuevo_contenido_salon,
                        ft.ElevatedButton(text="Actualizar")
                    ])
                )
            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            ################################################
            ft.Row([
                ft.Container(
                    content=self.tabla_institucion,
                    on_hover=datos_institucion
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Instituciones", size=30),
                        self.elegir_registro_institucion,
                        self.elegir_campo_institucion,
                        self.nuevo_contenido_institucion,
                        ft.ElevatedButton(text="Actualizar")
                    ])
                )
            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),

        ],
            scroll=ft.ScrollMode.ALWAYS
        )