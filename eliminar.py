import flet as ft
from base import Persona,Estudiante,Salon,Institucion,Relacion

class Eliminar(ft.UserControl):

    def obtener_personas(self):
        personas = Persona.leer()
        lista_personas = []
        for persona in personas:
            lista_personas.append(ft.dropdown.Option("CI: " + persona.split('--')[0] + " Nombre: " + persona.split('--')[1] + " Edad: " + persona.split('--')[2].replace('\n','')))
        return lista_personas
    
    def obtener_estudiantes(self):
        estudiantes = Estudiante.leer()
        lista_estudiantes = []
        for estudiante in estudiantes:
            lista_estudiantes.append(ft.dropdown.Option("CI: " + estudiante.split('--')[0] + " Grado: " + estudiante.split('--')[1] + " Seccion: " + estudiante.split('--')[2].replace('\n','')))
        return lista_estudiantes
    
    def obtener_salon(self):
        salones = Salon.leer()
        lista_salon = []
        for salon in salones:
            lista_salon.append(ft.dropdown.Option("ID_Salon: " + salon.split("--")[0] + " Seccion: " + salon.split("--")[1]))
        return lista_salon
    
    def obtener_institucion(self):
        instituciones = Institucion.leer()
        lista_instituciones = []
        for institucion in instituciones:
              lista_instituciones.append(ft.dropdown.Option("ID_Institucion: " + institucion.split("--")[0] + " Nombre: " + institucion.split("--")[1]))
        return lista_instituciones
      
    
    def build(self):        

        def actualizar_pagina(e):
            self.personas.options = self.obtener_personas()
            self.estudiante.options = self.obtener_estudiantes()
            self.salon.options = self.obtener_salon()
            self.institucion.options = self.obtener_institucion()
            self.update()

        def eliminar_persona(e):
            valor_a_eliminar = self.personas.value.split()[1]
            Persona.eliminar(identificador=valor_a_eliminar)
            Estudiante.eliminar(identificador=valor_a_eliminar)
            Relacion.eliminar(identificador=valor_a_eliminar)
            self.personas.options = self.obtener_personas()
            self.estudiante.options = self.obtener_estudiantes()
            self.personas.value = " "
            self.update()

        def eliminar_estudiante(e):
            valor_a_eliminar = self.estudiante.value.split()[1]
            Estudiante.eliminar(identificador=valor_a_eliminar)
            Relacion.eliminar(identificador=valor_a_eliminar)
            Persona.eliminar(identificador=valor_a_eliminar)
            self.estudiante.options = self.obtener_estudiantes()
            self.estudiante.value = " "
            self.update()
        
        def eliminar_salon(e):
            valor_a_eliminar = self.salon.value.split()[1]
            registro_b = self.salon.value.split()[3]
            Salon.eliminar_seccion(identificador=valor_a_eliminar,registro=str(registro_b))
            with open("relacion.txt","r") as validar:
                valor = validar.readlines
                if valor:
                    Relacion.eliminar(identificador=valor_a_eliminar)
            self.salon.options = self.obtener_salon()
            self.salon.value = " "
            self.update()

        def eliminar_institucion(e):
            valor_a_eliminar = self.institucion.value.split()[1]
            Institucion.eliminar(identificador=valor_a_eliminar)
            Relacion.eliminar(identificador=valor_a_eliminar)
            Salon.eliminar(identificador=valor_a_eliminar)
            self.institucion.options = self.obtener_institucion()
            self.salon.options = self.obtener_salon()
            self.institucion.value = " "
            self.update()

        # def actulizar_pagina(e):
        #     self.obtener_personas()
        #     self.obtener_institucion()
        #     self.obtener_estudiantes()
        #     self.obtener_salon()
        #     self.update()

        self.personas = ft.Dropdown(
            label = "Personas",
            hint_text = "Elija una persona a eliminar",
            options =self.obtener_personas()
        )
        self.estudiante = ft.Dropdown(
            label = "Estudiantes",
            hint_text= "Elija un estudiante a eliminar",
            options = self.obtener_estudiantes()
        )
        self.salon = ft.Dropdown(
            label = "Salon",
            hint_text= "Elija un Salon a eliminar",
            options=self.obtener_salon()
        )
        self.institucion = ft.Dropdown(
            label = "Institucion",
            hint_text= "Elija una institucion a eliminar",
            options=self.obtener_institucion()
        )
        return ft.Row(
            [
                ft.Column([
                    ft.Text("Personas",size=30),
                    ft.Container(
                        content=self.personas,
                        margin=10,
                        on_hover=actualizar_pagina
                    ),
                    ft.ElevatedButton(text="Eliminar", on_click=eliminar_persona)
                ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Column([
                    ft.Text("Estudiantes",size=30),
                    ft.Container(
                        content=self.estudiante,
                        margin=10,
                        on_hover=actualizar_pagina
                    ),
                    ft.ElevatedButton(text="Eliminar", on_click=eliminar_estudiante)
                ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Column([
                    ft.Text("Salon",size=30),
                    ft.Container(
                        content=self.salon,
                        margin=10,
                        on_hover=actualizar_pagina
                    ),
                    ft.ElevatedButton(text="Eliminar", on_click=eliminar_salon)
                ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Column([
                    ft.Text("Institucion",size=30),
                    ft.Container(
                        content=self.institucion,
                        margin=10,
                        on_hover=actualizar_pagina
                    ),
                    ft.ElevatedButton(text="Eliminar", on_click=eliminar_institucion)
                ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
                wrap=True,
                scroll=ft.ScrollMode.ALWAYS
            )

        # ft.Row([
        #     ft.Column([
        #         ft.Text("Personas"),
        #         ft.Container(
        #             content=self.personas,
        #             margin=10
        #         ),
        #         ft.ElevatedButton(text="Eliminar")
        #     ],
        #         alignment=ft.MainAxisAlignment.CENTER
        #     ),
        #     ft.Column([
        #         ft.Text("Estudiante"),
        #         ft.Container(
        #             content=self.estudiante,
        #             margin=10
        #         ),
        #         ft.ElevatedButton(text="Eliminar")
        #     ],
        #         alignment=ft.MainAxisAlignment.CENTER
        #     ),
        #     ft.Column([
        #         ft.Text("Salon"),
        #         ft.Container(
        #             content=self.salon,
        #             margin=10
        #         ),
        #         ft.ElevatedButton(text="Eliminar")
        #     ],
        #         alignment=ft.MainAxisAlignment.CENTER
        #     ),
        #     ft.Column([
        #         ft.Text("Institucion"),
        #         ft.Container(
        #             content=self.institucion,
        #             margin=10
        #         ),
        #         ft.ElevatedButton(text="Eliminar")
        #     ],
        #         alignment=ft.MainAxisAlignment.CENTER
        #     )
        # ],
        #     alignment=ft.MainAxisAlignment.CENTER,
        # )