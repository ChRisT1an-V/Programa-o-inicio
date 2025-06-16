import flet as ft
import random

def main(page: ft.Page):
    page.title = "Festa de São João"
    page.bgcolor = "#fffbe6"
    page.scroll = "auto"

    titulo = ft.Text("🎉 Viva São João! 🎉", size=30, weight="bold", color="#d17f00")
    mensagem = ft.Text(
        "Comidas típicas, danças, fogueiras e muita alegria!\n"
        "Que sua festa junina seja repleta de calor humano e diversão!",
        size=18,
        color="#333"
    )

    fogos_area = ft.Column()

    def acender_fogos(e):
        fogos_area.controls.clear()
        emojis_fogos = ["🎆", "🎇", "✨", "💥", "🔥"]
        for _ in range(10):
            emoji = random.choice(emojis_fogos)
            cor = random.choice(["red", "orange", "purple", "green", "blue"])
            fogos_area.controls.append(
                ft.Text(emoji, size=40, color=cor, text_align="center")
            )
        page.update()

    botao_fogos = ft.ElevatedButton(
        "Acender fogos 🎆", on_click=acender_fogos, color="white", bgcolor="#e65100"
    )

    page.add(
        ft.Column(
            [
                titulo,
                mensagem,
                botao_fogos,
                fogos_area
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
            spacing=20
        )
    )

ft.app(target=main)
