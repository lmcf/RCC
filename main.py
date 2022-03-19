# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:36:47 2022

@author: calde
"""

from functions import *

data = {
    'msg': 'INICIO :: {} del archivo {}',
    'args': [
        'Prueba',
        __file__
    ]
}

msglog(data, l.NAME_INFO)
from tkinter import *
from tkinter import ttk
from functools import partial


# Modulo de sistema
# Lo usaremos para desactivar el keystroke si hacemos hold en alguna tecla


# os.system('xset r off')

def App():
    global root
    # Instancioms la clase tkinter
    root = Tk()


    # Construimos la ventana usando una clase con toda la información
    deadlight = GUI(root)

    # Iniciamos bucle
    root.mainloop()


class GUI:

    def __init__(self, deadlight=None):

        # Configuramos dimension de la ventana, posición, background color y titulo
        deadlight.geometry("750x300+265+105")
        deadlight.configure(background=l.BG_COLOR)
        deadlight.title("RC Control")

        #
        self.onoff = False

        # Usaremos el widget style de tkinter para darle color a botones
        self.style = ttk.Style(root)

        # Ponemos el id y class de a quien le afectará
        # Y configuramos los colores iniciales
        self.style.configure('exitButton.TButton',
                             background=l.COLOR_DANGER,
                             foreground=l.COLOR_WHITE,
                             font=l.FONT_STYLE_TITLE,
                             width=10
                             )
        # En caso de hacer hover/active/focus... el boton cambiara el estilo
        self.style.map('exitButton.TButton',

                       background=[('active', l.COLOR_DANGER_ACTIVE)],

                       foreground=[],

                       highlightcolor=[],

                       relie=[('pressed', 'ridge')]

                       )

        # Configuramos los labels
        # Donde en función de lo que este haciendo el RC se pondra ver o no .
        # Es como una panel de control en el que ves lo que se activa y lo que se inactiva del RC

        self.lbl_up = Label(root, text="ACELERAR", bg=l.COLOR_INACTIVE, fg=l.COLOR_BLACK,
                            font=l.FONT_STYLE_TXT, width=l.LBL_FIXED_WIDTH)
        self.lbl_up.grid(pady=10, padx=5, row=2, column=3)

        self.lbl_back = Label(root, text="MARCHA ATRÁS", bg=l.COLOR_INACTIVE, fg=l.COLOR_BLACK,
                              font=l.FONT_STYLE_TXT, width=l.LBL_FIXED_WIDTH)
        self.lbl_back.grid(pady=10, padx=5, row=4, column=3)

        self.lbl_right = Label(root, text="GIRO DERECHA", bg=l.COLOR_INACTIVE, fg=l.COLOR_BLACK,
                               font=l.FONT_STYLE_TXT, width=l.LBL_FIXED_WIDTH)
        self.lbl_right.grid(pady=10, padx=5, row=3, column=4)

        self.lbl_left = Label(root, text="GIRO IZQUIERDA", bg=l.COLOR_INACTIVE, fg=l.COLOR_BLACK,
                              font=l.FONT_STYLE_TXT, width=l.LBL_FIXED_WIDTH)
        self.lbl_left.grid(pady=10, padx=5, row=3, column=2)

        # Botón de Salir
        self.btn_exit = ttk.Button(root,
                                   text='Exit',
                                   command=quit,
                                   style='exitButton.TButton')

        # Estilo botón salir
        self.btn_exit.grid(pady=10, padx=5, row=5, column=3)

        # Detecta que tecla se pulsa y se suelta
        # En función de lo que haga activar o desactivara motores
        root.bind("<KeyPress>", self.move_rc)
        root.bind("<KeyRelease>", self.move_rc)

    def move_rc(self, event):
        # Recogemos la telca pulsada
        key = event.keysym

        move_rc_on_debug = {
            'msg': 'Archvio: {} ### Funcion: {} ### Comando: {}',
            'args': [
                __name__,
                self.move_rc.__name__,
                str(key)
            ]
        }
        msglog(move_rc_on_debug)

        # Esta variable sirve para el control de errores
        # de cuando se activa/desactiva o no un motor
        release = False

        # Activamos funciones

        self.lbl_back.config(bg=l.COLOR_INACTIVE)
        self.lbl_left.config(bg=l.COLOR_INACTIVE)
        self.lbl_right.config(bg=l.COLOR_INACTIVE)

        self.onoff = False if self.onoff else True
        # motor1 = 0 - motor2 = 0

        if key == "Up":
            if self.onoff:
                self.lbl_up.config(bg=l.COLOR_SUCCESS)
                # otor1/Izquierdo = 1 - motor2/derecho = 1

            else:
                self.lbl_up.config(bg=l.COLOR_INACTIVE)
                # otor1/Izquierdo = 0 - motor2/derecho = 0

        elif key == 'Down':
            if self.onoff:
                self.lbl_back.config(bg=l.COLOR_SUCCESS)
                #  motor1/Izquierdo = -1 - motor2/derecho = -1

            else:
                self.lbl_back.config(bg=l.COLOR_INACTIVE)
                #  motor1/Izquierdo = 0 - motor2/derecho = 0

        elif key == 'Right':
            if self.onoff:
                self.lbl_right.config(bg=l.COLOR_SUCCESS)
                #  motor1/Izquierdo = 1 - motor2/derecho = -1

            else:
                self.lbl_right.config(bg=l.COLOR_INACTIVE)
                # motor1/Izquierdo = 0 - motor2/derecho = 0

        elif key == 'Left':
            if self.onoff:
                self.lbl_left.config(bg=l.COLOR_SUCCESS)
                #  motor1/Izquierdo = -1 - motor2/derecho = 1

            else:
                self.lbl_left.config(bg=l.COLOR_INACTIVE)
                # motor1/Izquierdo = 0 - motor2/derecho = 0

            # rc.turnUPDOWN_left(self, release)

if __name__ == '__main__':
    App()
