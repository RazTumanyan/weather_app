import flet as ft
import requests
from token import API


def main(page: ft.Page):
    page.title = "Weather App"
    page.theme_mode = "dark"
    page.window_width = 600
    page.window_height = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label="Write the Country", width=400)
    weather_data = ft.Text("")

    def get_info(e):
        if len(user_data.value) < 2:
            return

        URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric"
        res = requests.get(URL).json()
        temp = res['main']['temp']
        weather_data.value = "The Weather: " + str(temp)
        page.update()

    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text("Weather App")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text="Get", on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)

