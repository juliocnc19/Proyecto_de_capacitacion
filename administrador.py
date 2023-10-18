import flet as ft
from base import Persona,Estudiante,Salon,Institucion,Crud,Relacion
from crear import Crear
from actualizar import Actualizar
from eliminar import Eliminar

class Administrador(ft.UserControl):
    
    def build(self):
        def actualizar(e):
            self.update()
        
        return ft.Container(
            content=ft.Tabs(
                    selected_index=0,
                    animation_duration=300,
                    on_change=actualizar,
                    tabs=[
                        ft.Tab(
                            text="Crear",
                            content=Crear()
                        ),
                        ft.Tab(
                            text="Actualizar",
                            content=Actualizar()
                        ),
                        ft.Tab(
                            text="Eliminar",
                            content=Eliminar()
                        )
                        ],
                        expand=1,
                ),
        )