"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import asyncio
import reflex as rx

from rxconfig import config

segundos = 0
class State(rx.State):
# COLORES Y FONT COLOR
    text_color = "white"
    bg_color = "#DB001B"
#  TEXTOS
    titulo = "CRONOMETRO SALESIANO"
    boton_redireccion_cronometro = "CRONÓMETRO"
    boton_regreso_pagina_inicio = "INICIO"  
    boton_inicio_cronometro = "INICIAR"
    boton_pausa_cronometro = "PAUSA"
    boton_reinicio_cronometro = "REINICIO"
    boton_esborrar_cronometro = "BORRAR"
    texto_placeholder = "MINUTOS"
    boton_introduccion = "INTRODUCCIÓN"
    boton_exposicion = "EXPOSICIÓN DE ARGUMENTOS"
    boton_preguntas = "PREGUNTAS CRUZADAS"
    boton_conclusion = "CONLCUSIÓN"
    boton_cierre = "CIERRE"
    boton_crono_personalizado = "CRONÓMETRO PROPIO"
# PONER CERO A LOS TEMPORIZADORES
    poner_cero_intro: str = "0"
    poner_cero_intro_minutos: str = "0"
    poner_cero_exposicion: str = "0"
    poner_cero_exposicion_minutos: str = "0"
    poner_cero_preguntas: str = "0"
    poner_cero_preguntas_minutos: str = "0"
    poner_cero_conclusion: str = "0"
    poner_cero_conclusion_minutos: str = "0"
    poner_cero_cierre: str = "0"
    poner_cero_cierre_minutos: str = "0"
    poner_cero_crono_personalizado: str = "0"
    poner_cero_crono_personalizado_minutos: str = "0"
# SEGUNDOS RESTANTES TEMPORIZADORES
    segundos_restantes_intro: int = 180
    segundos_restantes_exposicion: int = 300
    segundos_restantes_preguntas: int = 360
    segundos_restantes_conclusion: int = 600
    segundos_restantes_cierre: int = 120
    segundos_restantes_crono_personalizado: int = segundos
# TEMPORIZADORES ACTIVOS
    esta_activo_intro: bool = False
    esta_activo_exposicion: bool = False
    esta_activo_preguntas: bool = False
    esta_activo_conclusion: bool = False
    esta_activo_cierre: bool = False
    esta_activo_crono_personalizado: bool = False
# BOTONES ACTIVOS
    intro: bool = True
    exposicion: bool = False
    preguntas: bool = False
    conclusion: bool = False
    cierre: bool = False
    crono_personalizado: bool = False

# TEMPORIZADOR INTRODUCCIÓN
    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_intro(self):
        async with self:
            self.esta_activo_intro = True
        while True:
            async with self:
                if not self.esta_activo_intro or self.segundos_restantes_intro == 0:
                    return
                self.segundos_restantes_intro -= 1
                if self.segundos_restantes_intro%60 < 10:
                    self.poner_cero_intro = "0"
                else:
                    self.poner_cero_intro = ""
                if self.segundos_restantes_intro//60 < 10:
                    self.poner_cero_intro_minutos = "0"
                else:
                    self.poner_cero_intro_minutos = ""
            await asyncio.sleep(1)
# TEMPORIZADOR EXPOSICIÓN DE ARGUMENTOS
    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_exposicion(self):
        async with self:
            self.esta_activo_exposicion = True
        while True:
            async with self:
                if not self.esta_activo_exposicion or self.segundos_restantes_exposicion == 0:
                    return
                self.segundos_restantes_exposicion -= 1
                if self.segundos_restantes_exposicion%60 < 10:
                    self.poner_cero_exposicion = "0"
                else:
                    self.poner_cero_exposicion = ""
                if self.segundos_restantes_exposicion//60 < 10:
                    self.poner_cero_exposicion_minutos = "0"
                else:
                    self.poner_cero_exposicion_minutos = ""
            await asyncio.sleep(1)
# TEMPORIZADOR PREGUNTAS CRUZADAS
    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_preguntas(self):
        async with self:
            self.esta_activo_preguntas = True
        while True:
            async with self:
                if not self.esta_activo_preguntas or self.segundos_restantes_preguntas == 0:
                    return
                self.segundos_restantes_preguntas -= 1
                if self.segundos_restantes_preguntas%60 < 10:
                    self.poner_cero_preguntas = "0"
                else:
                    self.poner_cero_preguntas = ""
                if self.segundos_restantes_preguntas//60 < 10:
                    self.poner_cero_preguntas_minutos = "0"
                else:
                    self.poner_cero_preguntas_minutos = ""
            await asyncio.sleep(1)
# TEMPORIZADOR CONLCUSIÓN
    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_conclusion(self):
        async with self:
            self.esta_activo_conclusion = True
        while True:
            async with self:
                if not self.esta_activo_conclusion or self.segundos_restantes_conclusion == 0:
                    return
                self.segundos_restantes_conclusion -= 1
                if self.segundos_restantes_conclusion%60 < 10:
                    self.poner_cero_conclusion = "0"
                else:
                    self.poner_cero_conclusion = ""
                if self.segundos_restantes_conclusion//60 < 10:
                    self.poner_cero_conclusion_minutos = "0"
                else:
                    self.poner_cero_conclusion_minutos = ""
            await asyncio.sleep(1)
# TEMPORIZADOR CIERRE
    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_cierre(self):
        async with self:
            self.esta_activo_cierre = True
        while True:
            async with self:
                if not self.esta_activo_cierre or self.segundos_restantes_cierre == 0:
                    return
                self.segundos_restantes_cierre -= 1
                if self.segundos_restantes_cierre%60 < 10:
                    self.poner_cero_cierre = "0"
                else:
                    self.poner_cero_cierre = ""
                if self.segundos_restantes_cierre//60 < 10:
                    self.poner_cero_cierre_minutos = "0"
                else:
                    self.poner_cero_cierre_minutos = ""
            await asyncio.sleep(1)
# TEMPORIZADOR CRONO PERSONALIZADO
    @rx.event(background=True)
    async def iniciar_cuenta_regresiva_crono_personalizado(self):
        async with self:
            self.esta_activo_crono_personalizado = True
        while True:
            async with self:
                if not self.esta_activo_crono_personalizado or self.segundos_restantes_crono_personalizado == 0:
                    return
                self.segundos_restantes_crono_personalizado -= 1
                if self.segundos_restantes_crono_personalizado%60 < 10:
                    self.poner_cero_crono_personalizado = "0"
                else:
                    self.poner_cero_crono_personalizado = ""
                if self.segundos_restantes_crono_personalizado//60 < 10:
                    self.poner_cero_crono_personalizado_minutos = "0"
                else:
                    self.poner_cero_crono_personalizado_minutos = ""
            await asyncio.sleep(1)

# RESTO EVENTOS
    # EVENTO DETENER (botón)
    @rx.event
    def detener(self):
        self.esta_activo_intro = False
        self.esta_activo_exposicion = False
        self.esta_activo_preguntas = False
        self.esta_activo_conclusion = False
        self.esta_activo_cierre = False
        self.esta_activo_crono_personalizado = False

    # EVENTO REINICIAR (botón)
    @rx.event
    def reiniciar(self):
# INTRO
        self.segundos_restantes_intro = 180
        self.esta_activo_intro = False
        self.poner_cero_intro = "0"
        self.poner_cero_intro_minutos = "0"
# EXPO
        self.segundos_restantes_exposicion = 300
        self.esta_activo_exposicion = False
        self.poner_cero_exposicion = "0"
        self.poner_cero_exposicion_minutos = "0"
# PREGUNTAS
        self.segundos_restantes_preguntas = 360
        self.esta_activo_preguntas = False
        self.poner_cero_preguntas = "0"
        self.poner_cero_preguntas_minutos = "0"
# CONCLUSION
        self.segundos_restantes_conclusion = 600
        self.esta_activo_conclusion = False
        self.poner_cero_conclusion = "0"
        self.poner_cero_conclusion_minutos = ""
        self.segundos_restantes_cierre = 120
# CIERRE
        self.esta_activo_cierre = False
        self.poner_cero_cierre = "0"
        self.poner_cero_cierre_minutos = "0"
# CRONO PERSONALIZADO
        self.esta_activo_crono_personalizado = False
        self.poner_cero_crono_personalizado = "0"
        self.poner_cero_crono_personalizado_minutos = "0"
        self.segundos_restantes_crono_personalizado = segundos

# EVENTO DE ACTIVAR LOS BOTONES PARA CAMBIAR EL FONDO
    # EVENTO INTRO
    @rx.event
    def intro_activo(self):
        self.intro = True
        self.exposicion = False
        self.preguntas = False
        self.conclusion = False
        self.cierre = False
        self.crono_personalizado = False
    # EVENTO EXPO
    @rx.event
    def exposicion_activo(self):
        self.intro = False
        self.exposicion = True
        self.preguntas = False
        self.conclusion = False
        self.cierre = False
        self.crono_personalizado = False
    # EVENTO PREGUNTAS
    @rx.event
    def preguntas_activo(self):
        self.intro = False
        self.exposicion = False
        self.preguntas = True
        self.conclusion = False
        self.cierre = False
        self.crono_personalizado = False
    # EVENT CONCLUSIÓN
    @rx.event
    def conclusion_activo(self):
        self.intro = False
        self.exposicion = False
        self.preguntas = False
        self.conclusion = True
        self.cierre = False
        self.crono_personalizado = False
    # EVENTO CIERRE
    @rx.event
    def cierre_activo(self):
        self.intro = False
        self.exposicion = False
        self.preguntas = False
        self.conclusion = False 
        self.cierre = True
        self.crono_personalizado = False
    # EVENTO CRONO PERSONALIZADO
    @rx.event
    def crono_personalizado_activo(self):
        self.intro = False
        self.exposicion = False
        self.preguntas = False
        self.conclusion = False 
        self.cierre = False
        self.crono_personalizado = True


    # EVENTO SET SEGUNDOS CRONO PERSONALIZADO
    @rx.event
    def set_segundos_crono_personalizado(self, valor):
        self.segundos_restantes_crono_personalizado = int(valor)
        self.segundos_restantes_crono_personalizado = set(self.segundos_restantes_crono_personalizado) 

# TRADUCCIONES
    # EVENTO TRADUCCIÓN VALENCIANO
    @rx.event
    def valenciano(self):
        self.titulo = "CRONÒMETRE SALESIÀ"
        self.boton_redireccion_cronometro = "CRONÒMETRE"
        self.boton_regreso_pagina_inicio = "INICI"  
        self.boton_inicio_cronometro = "INICIAR"
        self.boton_pausa_cronometro = "PAUSAR"
        self.boton_reinicio_cronometro = "REINICIAR"
        self.boton_esborrar_cronometro = "ESBORRAR"
        self.texto_placeholder = "INTRODUÏR SEGONS"
        self.boton_introduccion = "INTRODUCCIÓ"
        self.boton_exposicion = "EXPOSICIÓ D'ARGUMENTS"
        self.boton_preguntas = "PREGUNTES CREUADES"
        self.boton_conclusion = "CONLCUSIÓ"
        self.boton_cierre = "TANCADA"
        self.boton_crono_personalizado = "CRONÒMETRE PROPI"
    # EVENTO TRADUCCIÓN CASTELLANO
    @rx.event
    def castellano(self):
        self.titulo = "CRONOMETRO SALESIANO"
        self.boton_redireccion_cronometro = "CRONÓMETRO"
        self.boton_regreso_pagina_inicio = "INICIO"  
        self.boton_inicio_cronometro = "INICIAR"
        self.boton_pausa_cronometro = "PAUSAR"
        self.boton_reinicio_cronometro = "REINICIAR"
        self.boton_esborrar_cronometro = "BORRAR"
        self.boton_introduccion = "INTRODUCCIÓN"
        self.boton_exposicion = "EXPOSICIÓN DE ARGUMENTOS"
        self.boton_preguntas = "PREGUNTAS CRUZADAS"
        self.boton_conclusion = "CONLCUSIÓN"
        self.boton_cierre = "CIERRE"
        self.boton_crono_personalizado = "CRONÓMETRO PROPIO"
        self.texto_placeholder = "INTRODUCIR SEGUNDOS"
    

#def set_segundos(segundos) -> rx.Component:
#    return rx.vstack(
#        rx.heading(State.segundos_restantes_crono_personalizado),
#        rx.input(
#            placeholder="Search here...",
#            value=segundos,
#            on_change=State.segundos_restantes_crono_personalizado.set_text,
#        ),
#    )

# PÁGINA INICIAL
def Inici() -> rx.Component:
    # Welcome Page (Index)
    return rx.container( 
        rx.vstack(
            rx.flex(
                rx.hstack(
                    rx.heading(State.titulo, font_size="50px", justify_content="40%", margin="30px", style={"align-self": "center", "position": "absolute", "right": "60vh"}),
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
                            "right": "200px"}
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
    
#PÁGINA CRONOMETRO
def cronometre() -> rx.Component:
    return rx.container(
        rx.vstack(
# STACK CON LA PARTE SUPERIOR
            rx.hstack(
                rx.button(State.boton_regreso_pagina_inicio,
                font_size="20px",
                justify_content="center",
                margin="30px",
                style={
                    "align-self": "center", "width": "120px", "height": "80px","background-color": State.bg_color, "color": State.text_color,
                    "border": "2px solid white", "border-radius": "10px", "position": "absolute", "left": "0"},
                on_click=lambda: rx.redirect("/")),
                rx.spacer(),
                rx.heading(State.titulo, font_size="50px", justify_content="40%", margin="30%", style={"align-self": "center", "position": "absolute", "right": "40px"}),
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
                            "right": "200px"}
                    ),
                rx.image(src="/logo_sales.png", style={"height": "16.67vh", "position": "absolute", "right": "0", "top": "0"}),
                style= {"width": "100%","height": "100px"},               
            ),
# STACK CON LOS 5 BOTONES, PARA HACER EL CONDICIONAL
            rx.hstack(
                rx.cond(State.crono_personalizado,
                    rx.button(State.boton_crono_personalizado, font_size="20px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                    "width": "190px", "height": "60px", "background-color": "#A00015","color": State.text_color, "border": "2px solid white", "border-radius": "10px"}, 
                        on_click=lambda: State.crono_personalizado_activo()),
                    rx.button(State.boton_crono_personalizado, font_size="20px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                    "width": "190px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                        on_click=lambda: State.crono_personalizado_activo())),
                rx.cond(State.intro,
                    rx.button(State.boton_introduccion, font_size="20px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                    "width": "190px", "height": "60px", "background-color": "#A00015","color": State.text_color, "border": "2px solid white", "border-radius": "10px"}, 
                    on_click=lambda: State.intro_activo()),
                    rx.button(State.boton_introduccion, font_size="20px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                    "width": "190px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.intro_activo()),),
                rx.cond(State.exposicion,
                rx.button(State.boton_exposicion, font_size="15px", justify_content="center", margin="0 10px",style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": "#A00015","color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.exposicion_activo()),
                rx.button(State.boton_exposicion, font_size="15px", justify_content="center", margin="0 10px",style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.exposicion_activo())
                ),
                rx.cond(State.preguntas,
                rx.button(State.boton_preguntas, font_size="15px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": "#A00015","color": State.text_color, "border": "2px solid white","border-radius": "10px"},
                    on_click=lambda: State.preguntas_activo()),
                rx.button(State.boton_preguntas, font_size="15px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white","border-radius": "10px"},
                    on_click=lambda: State.preguntas_activo())
                ),
                rx.cond(State.conclusion,
                rx.button(State.boton_conclusion, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": "#A00015","color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.conclusion_activo()),
                rx.button(State.boton_conclusion, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.conclusion_activo())
                ),
                rx.cond(State.cierre,
                rx.button(State.boton_cierre, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": "#A00015","color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.cierre_activo()),
                rx.button(State.boton_cierre, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center",
                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                    on_click=lambda: State.cierre_activo()),
                ),
                style={"justify-content": "center", "margin-top": "75px", "width": "100%", "gap": "20px"},   
            ),
# CAMBIAR EL HEADING DEL TEMPORIZADOR, TAMBIÉN CON OTRO CONDICIONAL
            rx.cond(State.crono_personalizado,
                rx.heading(State.poner_cero_crono_personalizado_minutos, State.segundos_restantes_crono_personalizado//60, ":", State.poner_cero_crono_personalizado, State.segundos_restantes_crono_personalizado%60, font_size="60px", justify_content="center",
                style={"align-self": "center", "width": "50hv", "height": "60px", "background-color": State.bg_color, "color": State.text_color, "margin-top": "150px"}),
                rx.cond(State.intro,
                    rx.heading(State.poner_cero_intro_minutos,State.segundos_restantes_intro//60, ":", State.poner_cero_intro, State.segundos_restantes_intro%60, font_size="60px", justify_content="center", style={"align-self": "center",     
                    "width": "50hv", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "margin-top": "150px"}),
                    rx.cond(State.exposicion,
                        rx.heading(State.poner_cero_exposicion_minutos, State.segundos_restantes_exposicion//60, ":", State.poner_cero_exposicion, State.segundos_restantes_exposicion%60, font_size="60px", justify_content="center", style={"align-self": "center",     
                        "width": "50hv", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "margin-top": "150px"}),
                        rx.cond(State.preguntas,
                            rx.heading(State.poner_cero_preguntas_minutos, State.segundos_restantes_preguntas//60, ":", State.poner_cero_preguntas, State.segundos_restantes_preguntas%60, font_size="60px", justify_content="center", style={"align-self": "center",     
                            "width": "50hv", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "margin-top": "150px"}),
                            rx.cond(State.conclusion,
                                rx.heading(State.poner_cero_conclusion_minutos, State.segundos_restantes_conclusion//60, ":", State.poner_cero_conclusion, State.segundos_restantes_conclusion%60, font_size="60px", justify_content="center", style={"align-self": "center",     
                                "width": "50hv", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "margin-top": "150px"}),
                                rx.cond(State.cierre,
                                    rx.heading(State.poner_cero_cierre_minutos, State.segundos_restantes_cierre//60, ":", State.poner_cero_cierre, State.segundos_restantes_cierre%60, font_size="60px", justify_content="center", style={"align-self": "center",     
                                    "width": "50hv", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "margin-top": "150px"}),
                                ),
                            ),
                        ),
                    ),
                ),
        ),
# BOTONES DE INICIO, PAUSA Y REINICIO DEL TEMPORIZADOR, CON OTRO CONDICIONAL
            rx.cond(State.crono_personalizado,
                rx.hstack(
                    rx.input(id="Segundos",font_size="15px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                    "width": "190px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white"}, placeholder=State.texto_placeholder, value=0, type="number",
                    on_change=State.set_segundos_crono_personalizado()),
                    rx.cond(State.esta_activo_crono_personalizado,
                        rx.button(State.boton_pausa_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                        "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                            on_click=lambda: State.detener()),
                        rx.button(State.boton_inicio_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                        "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                            on_click=lambda: State.iniciar_cuenta_regresiva_crono_personalizado()),
                        ),
                        rx.button(State.boton_reinicio_cronometro,font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                        "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                            on_click=lambda: State.reiniciar()),
                        rx.button(State.boton_esborrar_cronometro, on_click=rx.set_value("Segundos", ""), style={"align-self": "center", "width": "100px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"}),
                        style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "100px", "margin-left": "25px"}),
                rx.cond(State.intro,
                    rx.hstack(
                            rx.cond(State.esta_activo_intro,
                                rx.button(State.boton_pausa_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                    on_click=lambda: State.detener()),
                                rx.button(State.boton_inicio_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                    on_click=lambda: State.iniciar_cuenta_regresiva_intro()),
                            ),
                            rx.button(State.boton_reinicio_cronometro,font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                            "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                on_click=lambda: State.reiniciar()),
                        style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "100px", "margin-left": "235px"}),    
                    rx.cond(State.exposicion,
                        rx.hstack(
                            rx.cond(State.esta_activo_exposicion,
                                    rx.button(State.boton_pausa_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                    "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                        on_click=lambda: State.detener()),
                                    rx.button(State.boton_inicio_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                    "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                        on_click=lambda: State.iniciar_cuenta_regresiva_exposicion()),),
                            rx.button(State.boton_reinicio_cronometro,font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                            "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                on_click=lambda: State.reiniciar()),
                            style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "100px", "margin-left": "235px"}),
                        rx.cond(State.preguntas,
                            rx.hstack(
                                rx.cond(State.esta_activo_preguntas,
                                    rx.button(State.boton_pausa_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                    "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                        on_click=lambda: State.detener()),
                                    rx.button(State.boton_inicio_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                    "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                        on_click=lambda: State.iniciar_cuenta_regresiva_preguntas())),
                                rx.button(State.boton_reinicio_cronometro,font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                    on_click=lambda: State.reiniciar()),
                            style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "100px", "margin-left": "235px"}),
                            rx.cond(State.conclusion,
                                rx.hstack(
                                    rx.cond(State.esta_activo_conclusion,
                                        rx.button(State.boton_pausa_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                        "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                            on_click=lambda: State.detener()),
                                        rx.button(State.boton_inicio_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                        "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                            on_click=lambda: State.iniciar_cuenta_regresiva_conclusion())),
                                    rx.button(State.boton_reinicio_cronometro,font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                    "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                        on_click=lambda: State.reiniciar()),
                                        style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "100px", "margin-left": "235px"}),
                                rx.cond(State.cierre,
                                    rx.hstack(
                                        rx.cond(State.esta_activo_cierre,
                                            rx.button(State.boton_pausa_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                            "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                                on_click=lambda: State.detener()),
                                            rx.button(State.boton_inicio_cronometro, font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                            "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                                on_click=lambda: State.iniciar_cuenta_regresiva_cierre())),
                                        rx.button(State.boton_reinicio_cronometro,font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                                        "width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"},
                                            on_click=lambda: State.reiniciar()),
                                    style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "100px", "margin-left": "235px"}),
                                ),
                            ),
                        ),
                    ),        
                ),
            ),
        ),
        style={"background-color": State.bg_color, "color": State.text_color, "height": "100vh", "widht": "100vw", "display": "flex", "flex-direction": "column"},
    )

                    #rx.input(id="segundos",font_size="25px", justify_content="center", margin="0 10px", style={"align-self": "center", 
                    #"width": "180px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white"}, placeholder="segundos",
                    #    on_change=lambda segundos: State.set_segundos((segundos))),
                    #rx.button(State.boton_esborrar_cronometro, on_click=rx.set_value("segundos", ""), style={"align-self": "center", "width": "100px", "height": "60px", "background-color": State.bg_color,"color": State.text_color, "border": "2px solid white", "border-radius": "10px"}),
                    #style={"justify-content": "space-between", "width": "100hv", "height": "100hv", "margin-top": "200px"}

app = rx.App()
app.add_page(Inici, route="/")
app.add_page(cronometre, route="/crono")    