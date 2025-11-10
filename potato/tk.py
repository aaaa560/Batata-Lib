import tkinter
from tkinter import Tk
from typing import Any


def criar_janela(titulo: str, largura: int, altura: int) -> Tk:
    root = tkinter.Tk()
    root.title(titulo)
    root.geometry(f'{largura}x{altura}')
    return root

def mostrar_janela(janela: tkinter.Tk) -> None:
    janela.mainloop()

def add_botao(janela: tkinter.Tk, texto: str, comando: Any) -> tkinter.Button:
    botao = tkinter.Button(janela, text=texto, command=comando)
    botao.pack()
    return botao

def add_label(janela: tkinter.Tk, texto: str) -> tkinter.Label:
    label = tkinter.Label(janela, text=texto)
    label.pack()
    return label

def add_entrada(janela: tkinter.Tk, texto: str) -> tkinter.Entry:
    entrada = tkinter.Entry(janela)
    entrada.insert(0, texto)
    entrada.pack()
    return entrada

def add_check_box(janela: tkinter.Tk, texto: str, variavel: Any) -> tkinter.Checkbutton:
    checkbutton = tkinter.Checkbutton(janela, text=texto, variable=variavel)
    checkbutton.pack()
    return checkbutton