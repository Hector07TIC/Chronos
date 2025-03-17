"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import asyncio
import reflex as rx

from rxconfig import config

bg_color = "#DB001B"
text_color = "white"
segundos = 60
class State(rx.State):
    segundos_restantes: int = segundos
    esta_activo: bool = False

    @rx.event(background=True)
    async def iniciar_cuenta_regresiva(self):
        async with self:
            self.esta_activo = True
        while True:
            async with self:
                if not self.esta_activo or self.segundos_restantes == 0:
                    return
                self.segundos_restantes -= 1
            await asyncio.sleep(1)

    @rx.event
    def detener(self):
        self.esta_activo = False

    @rx.event
    def reiniciar(self):
        self.segundos_restantes = segundos
        self.esta_activo = False

    @rx.event
    def set_segundos(self, valor):
        self.segundos_restantes = int(valor)

    
class Set_segundos(rx.State):
    text: str = f"{State.segundos_restantes} segundos restantes"


def set_segundos() -> rx.Component:
    return rx.vstack(
        rx.heading(Set_segundos),
        rx.input(
            placeholder="Search here...",
            value=Set_segundos,
            on_change=Set_segundos.set_text,
        ),
    )


def Inici() -> rx.Component:
    # Welcome Page (Index)
    return rx.container( 
        rx.vstack(
            rx.flex(
                rx.hstack(
                    rx.heading("CRONÒMETRE SALESIÀ", font_size="50px", justify_content="40%", margin="30px", style={"align-self": "center", "position": "relative"}),
                    rx.image(src="/logo_sales.png", style={"height": "16.67vh", "position": "absolute", "right": "0", "top": "0"}),
                    style= {"width": "100%","height": "100px"},               
                ),
            ),
            rx.image(src="/somos-futuro.jpg", style={"height": "50vh", "align-self": "center", "margin-top": "35px"}),
            rx.button( "CRONÒMETRE",
                font_size="35px",
                justify_content="center",
                margin="10%",
                style={
                    "align-self": "center",
                    "width": "40%",  # Aumentar el ancho del botón
                    "height": "60px",  # Aumentar la altura del botón
                    "background-color": bg_color,
                    "color": text_color,
                    "border": "2px solid white",  # Agregar un borde blanco
                    "border-radius": "10px"  # Agregar bordes redondeados
                },
                on_click=lambda: rx.redirect("/crono")
  # Navegar a la página "crono" al hacer clic 
            ),
        ),
    style={"background-color": bg_color, "color": text_color, "height": "100vh", "widht": "100vw", "display": "flex", "flex-direction": "column", "align-items": "center"},
    )
    
def cronometre() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.button( "INICI",
                font_size="20px",
                justify_content="center",
                margin="30px",
                style={
                    "align-self": "center", "width": "120px", "height": "80px","background-color": bg_color, "color": text_color,
                    "border": "2px solid white", "border-radius": "10px", "position": "absolute", "left": "0"},
                on_click=lambda: rx.redirect("/")),
                rx.spacer(),
                rx.heading("CRONÒMETRE SALESIÀ", font_size="50px", justify_content="40%", margin="30px", style={"align-self": "center", "position": "absolute"}),
                rx.spacer(),
                rx.image(src="/logo_sales.png", style={"height": "16.67vh", "position": "absolute", "right": "0", "top": "0"}),
                style= {"width": "100%","height": "100px"},               
            ),
            rx.hstack(
                rx.button("INTRODUCCIÒ", font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(180)),
                rx.button("EXPOSICIÓ D'ARGUMENTS", font_size="15px", justify_content="center", margin="0 10px",style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(300)),
                rx.button("PREGUNTES CREUADES", font_size="15px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white","border-radius": "10px"},
                    on_click=lambda: State.set_segundos(360)),
                rx.button("CONLCUSIÒ", font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(600)),
                rx.button("TANCADA", font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(120)),
                style={"justify-content": "space-between", "width": "100hv"}
            ),
            rx.heading(f"{State.segundos_restantes} segons restants", font_size="60px", justify_content="center", style={"align-self": "center", 
            "width": "50hv", "height": "60px", "background-color": bg_color,"color": text_color, "margin-top": "200px"}),
            rx.hstack(
                rx.button("INICIAR", font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.iniciar_cuenta_regresiva()),
                rx.button("PAUSAR", font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.detener()),
                rx.button("REINICIAR",font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.reiniciar()),
                rx.input(id="SEGONS",font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white"}, placeholder="SEGONS",
                    on_change=lambda segundos: State.set_segundos((segundos))),
                rx.button("ESBORRAR ", on_click=rx.set_value("SEGONS", ""), style={"align-self": "center", "width": "100px", "height": "60px", "background-color": bg_color,"color": text_color, "border": "2px solid white", "border-radius": "10px"}),
                style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "250px"}
            ),    
        ),
        style={"background-color": bg_color, "color": text_color, "height": "100vh", "widht": "100vw", "display": "flex", "flex-direction": "column"},
    )

app = rx.App()
app.add_page(Inici, route="/")
app.add_page(cronometre, route="/crono")