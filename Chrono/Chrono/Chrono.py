import asyncio
import reflex as rx

from rxconfig import config

segundos = 60
segundos_restantes: int = segundos
class State(rx.State):
    text_color = "white"
    bg_color = "#DB001B"
    titulo = "CRONOMETRO SALESIANO"
    boton_redireccion_cronometro = "CRONÓMETRO"
    boton_regreso_pagina_inicio = "INICIO"  
    boton_inicio_cronometro = "INICIAR"
    boton_pausa_cronometro = "PAUSA"
    boton_reinicio_cronometro = "REINICIO"
    boton_esborrar_cronometro = "BORRAR"
    placholder_segundos = "SEGUNDOS"
    boton_introduccion = "INTRODUCCIÓN"
    boton_exposicion = "EXPOSICIÓN DE ARGUMENTOS"
    boton_preguntas = "PREGUNTAS CRUZADAS"
    boton_conlcusion = "CONLCUSIÓN"
    boton_cierre = "CIERRE"
    segundos_restantes: int = segundos
    esta_activo: bool = False
    poner_cero = "0"

    @rx.event(background=True)
    async def iniciar_cuenta_regresiva(self):
        async with self:
            self.esta_activo = True
        while True:
            async with self:
                if not self.esta_activo or self.segundos_restantes == 0:
                    return
                self.segundos_restantes -= 1
                if self.segundos_restantes%60 < 10:
                    self.poner_cero = "0"
                else:
                    self.poner_cero = ""
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

    @rx.event
    def valenciano(self):
        self.titulo = "CRONÒMETRE SALESIÀ"
        self.boton_redireccion_cronometro = "CRONÒMETRE"
        self.boton_regreso_pagina_inicio = "INICI"  
        self.boton_inicio_cronometro = "INICIAR"
        self.boton_pausa_cronometro = "PAUSAR"
        self.boton_reinicio_cronometro = "REINICIAR"
        self.boton_esborrar_cronometro = "ESBORRAR"
        self.placholder_segundos = "SEGONS"
        self.boton_introduccion = "INTRODUCCIÓ"
        self.boton_exposicion = "EXPOSICIÓ D'ARGUMENTS"
        self.boton_preguntas = "PREGUNTES CREUADES"
        self.boton_conlcusion = "CONLCUSIÓ"
        self.boton_cierre = "TANCADA"

    @rx.event
    def castellano(self):
        self.titulo = "CRONOMETRO SALESIANO"
        self.boton_redireccion_cronometro = "CRONÓMETRO"
        self.boton_regreso_pagina_inicio = "INICIO"  
        self.boton_inicio_cronometro = "INICIAR"
        self.boton_pausa_cronometro = "PAUSAR"
        self.boton_reinicio_cronometro = "REINICIAR"
        self.boton_esborrar_cronometro = "BORRAR"
        self.placholder_segundos = "SEGUNDOS"
        self.boton_introduccion = "INTRODUCCIÓN"
        self.boton_exposicion = "EXPOSICIÓN DE ARGUMENTOS"
        self.boton_preguntas = "PREGUNTAS CRUZADAS"
        self.boton_conlcusion = "CONLCUSIÓN"
        self.boton_cierre = "CIERRE"
    
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
                    rx.heading(State.titulo, font_size="50px", justify_content="40%", margin="30px", style={"align-self": "center", "position": "relative"}),
                    rx.vstack(    
                        rx.button("Castellano", justify_content="center", font_size= "15px", margin="10%",
                            style={
                                "align-self": "flex-start",
                                "width": "100px",  
                                "height": "40px",  
                                "background-color": State.bg_color,
                                "color": State.text_color,
                                "border": "2px solid white",  
                                "border-radius": "10px",  
                            },
                            on_click=lambda: State.castellano()),
                        rx.button("Valenciano", justify_content="center", font_size= "15px", margin="10%",
                            style={
                                "align-self": "flex-start",
                                "width": "100px",  
                                "height": "40px",  
                                "background-color": State.bg_color,
                                "color": State.text_color,
                                "border": "2px solid white",  
                                "border-radius": "10px"  
                            },
                            on_click=lambda: State.valenciano()),
                        style={"position": "absolute",
                            "top": "10px",
                            "right": "150px"}
                    ),
                    rx.image(src="/logo_sales.png", style={"height": "16.67vh", "position": "absolute", "right": "0", "top": "0"}),
                    style= {"width": "100%","height": "100px"},               
                ),
            ),
            rx.image(src="/somos-futuro.jpg", style={"height": "50vh", "align-self": "center", "margin-top": "35px"}),
            rx.button( State.boton_redireccion_cronometro,
                font_size="35px",
                justify_content="center",
                margin="10%",
                style={
                    "align-self": "center",
                    "width": "40%",  # Aumentar el ancho del botón
                    "height": "60px",  # Aumentar la altura del botón
                    "background-color": State.bg_color,
                    "color": State.text_color,
                    "border": "2px solid white",  # Agregar un borde blanco
                    "border-radius": "10px"  # Agregar bordes redondeados
                },
                on_click=lambda: rx.redirect("/crono")
  # Navegar a la página "crono" al hacer clic 
            ),
        ),
    style={"background-color": State.bg_color, "color": State.text_color, "height": "100vh", "widht": "100vw", "display": "flex", "flex-direction": "column", "align-items": "center"},
    )
    
def cronometre() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.button( State.boton_regreso_pagina_inicio,
                font_size="20px",
                justify_content="center",
                margin="30px",
                style={
                    "align-self": "center", "width": "120px", "height": "80px","background-color": State.bg_color, "color": State.text_color,
                    "border": "2px solid white", "border-radius": "10px", "position": "absolute", "left": "0"},
                on_click=lambda: rx.redirect("/")),
                rx.spacer(),
                rx.heading(State.titulo, font_size="50px", justify_content="40%", margin="30px", style={"align-self": "center", "position": "absolute"}),
                rx.vstack(    
                        rx.button("Castellano", justify_content="center", font_size= "15px", margin="10%",
                            style={
                                "align-self": "flex-start",
                                "width": "100px",  
                                "height": "40px",  
                                "background-color": State.bg_color,
                                "color": State.text_color,
                                "border": "2px solid white",  
                                "border-radius": "10px",  
                            },
                            on_click=lambda: State.castellano()),
                        rx.button("Valenciano", justify_content="center", font_size= "15px", margin="10%",
                            style={
                                "align-self": "flex-start",
                                "width": "100px",  
                                "height": "40px",  
                                "background-color": State.bg_color,
                                "color": State.text_color,
                                "border": "2px solid white",  
                                "border-radius": "10px"  
                            },
                            on_click=lambda: State.valenciano()),
                        style={"position": "absolute",
                            "top": "10px",
                            "right": "150px"}
                    ),
                rx.image(src="/logo_sales.png", style={"height": "16.67vh", "position": "absolute", "right": "0", "top": "0"}),
                style= {"width": "100%","height": "100px"},               
            ),
            rx.hstack(
                rx.button(State.boton_introduccion, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "190px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(180)),
                rx.button(State.boton_exposicion, font_size="15px", justify_content="center", margin="0 10px",style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(300)),
                rx.button(State.boton_preguntas, font_size="15px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white","border-radius": "10px"},
                    on_click=lambda: State.set_segundos(360)),
                rx.button(State.boton_conlcusion, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(600)),
                rx.button(State.boton_cierre, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.set_segundos(120)),
                style={"justify-content": "space-between", "width": "100hv", "margin-top": "50px"}
            ),
            rx.heading("0",State.segundos_restantes//60, ":", State.poner_cero, State.segundos_restantes%60, font_size="60px", justify_content="center", style={"align-self": "center",     
            "width": "50hv", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "margin-top": "150px"}),
            rx.hstack(
                rx.button(State.boton_inicio_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.iniciar_cuenta_regresiva()),
                rx.button(State.boton_pausa_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.detener()),
                rx.button(State.boton_reinicio_cronometro,font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.reiniciar()),
                rx.input(id="segundos",font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white"}, placeholder="segundos",
                    on_change=lambda segundos: State.set_segundos((segundos))),
                rx.button(State.boton_esborrar_cronometro, on_click=rx.set_value("segundos", ""), style={"align-self": "center", "width": "100px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"}),
                style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "200px"}
            ),    
        ),
        style={"background-color": State.bg_color, "color": State.text_color, "height": "100vh", "widht": "100vw", "display": "flex", "flex-direction": "column"},
    )

app = rx.App()
app.add_page(Inici, route="/")
app.add_page(cronometre, route="/crono")