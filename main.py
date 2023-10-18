import flet as ft
from base import Persona,Estudiante,Salon,Institucion,Crud
from analista import Analista
from administrador import Administrador


def main(page: ft.Page):
    page.title = "JULIOOO"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    ventana = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Administrador",
                content=Administrador()
            ),
            ft.Tab(
                text="Analista",
                content=Analista()
            )
        ],
        expand=1,
    )

    page.add(ventana)

#t.app(target=main, view=ft.AppView.WEB_BROWSER)
ft.app(target=main)