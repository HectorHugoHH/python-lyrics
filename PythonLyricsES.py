
import tkinter as tk

from tkinter import messagebox


def guardartitulo():
    global titulo
    titulo = cajatitulo.get()
    abrirventanacantar()



def abrirventanacantar():
    global ventanacantar, cajaletra, botonletra

    ventanacantar = tk.Toplevel(ventanas)
    ventanacantar.title("Letra")

    indicacioncantar = tk.Message(ventanacantar, text="Copia y pega la letra de la cancion, separada en versos")
    indicacioncantar.pack()

    botonletra = tk.Button(ventanacantar, text="Cantar", command=guardarletra)
    botonletra.pack()

    botonsalircantar = tk.Button(ventanacantar, text="Salir", command=salir)
    botonsalircantar.pack()

    cajaletra = tk.Text(ventanacantar)
    cajaletra.pack()

def cantar(titulo):
    with open("letra.txt", "r") as l:
        letra = l.readlines()
    for parte in letra:
        if parte.strip() != "":
            messagebox.showinfo(titulo, parte)
        else:
            messagebox.showinfo(titulo, "*Musica*")

def guardarletra():
    letra = cajaletra.get(1.0,"end")
    with open("letra.txt", "w") as l:
        l.write(letra)
    botonletra.config(state="disabled")
    cantar(titulo)
    ventanacantar.destroy()

def salir():
    ventanas.destroy()



ventanas = tk.Tk()

ventanas.title("Titulo")

ventanatitulo = ventanas

indicaciontitulo = tk.Message(ventanatitulo, text="Escribe el titulo de la cancion")
indicaciontitulo.pack()

botontitulo = tk.Button(ventanatitulo, text="Siguiente", command=guardartitulo)
botontitulo.pack()

botonsalir = tk.Button(ventanatitulo, text="Salir", command=salir)
botonsalir.pack()

cajatitulo = tk.Entry(ventanatitulo)
cajatitulo.pack()

ventanas.mainloop()





