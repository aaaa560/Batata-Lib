from tkinter import Tk, Button, Entry, Label, Checkbutton
from typing import Any


def criar_janela(titulo: str, largura: int, altura: int) -> Tk:
    root = Tk()
    root.title(titulo)
    root.geometry(f'{largura}x{altura}')
    return root


def mostrar_janela(janela: Tk) -> None:
    janela.mainloop()


def add_botao(janela: Tk, texto: str, comando: Any) -> Button:
    botao = Button(janela, text=texto, command=comando)
    botao.pack()
    return botao


def add_label(janela: Tk, texto: str) -> Label:
    label = Label(janela, text=texto)
    label.pack()
    return label


def add_entrada(janela: Tk, texto: str) -> Entry:
    entrada = Entry(janela)
    entrada.insert(0, texto)
    entrada.pack()
    return entrada


def add_check_box(janela: Tk, texto: str, variavel: Any) -> Checkbutton:
    checkbutton = Checkbutton(janela, text=texto, variable=variavel)
    checkbutton.pack()
    return checkbutton
