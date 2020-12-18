from tkinter import *
from googlesearch import search

# Creacion de la ventana y los label
global ventana
ventana = Tk()
ventana.geometry("600x500+400+125")
ventana.title("Mini-Goo")
ventana.iconbitmap("mini-goo.ico")
ventana.config(background="#000000")
Titulo = Label(text="Mini-Goo", font=("Cambria", 20), bg="#24b43c", fg="white", width="500", height="2")
Titulo.pack()
Titulo1 = Label(text="Creador: N05TR@  Version: 1.0", font=("Cambria", 10), bg="#24b43c", fg="white", width="500", height="1")
Titulo1.pack()
Titulo1 = Label(text="", font=("Cambria", 15), bg="#24b43c", fg="white", width="500", height="1")
Titulo1.place(x = 0, y = 455)

# Agregandole una imagen
image = PhotoImage(file="mini-goo.gif")
image = image.subsample(2, 2)
label = Label(image=image)
label.place(x=450, y=10)

# Variable principal
buscar = StringVar()

# Creando funcion para abrir una sub ventada del boton "acerca de" dentro del menu "Informacion"
def acerca_de():
    global SubVentana
    SubVentana = Toplevel(ventana)
    SubVentana.geometry("600x500+400+125")
    SubVentana.title("Acerca de")
    SubVentana.iconbitmap("mini-goo.ico")
    SubVentana.config(background="#000000")


    SubVentana.mainloop()



# Creando barra de menu
menubarra = Menu(ventana)
ventana.config(menu = menubarra)
filemenu = Menu(menubarra)
filemenu = Menu(menubarra, tearoff=0)
filemenu.add_command(label="Acerca de", command = acerca_de)
filemenu.add_separator()
filemenu.add_command(label="Salir", command = ventana.quit)
menubarra.add_cascade(label = "Opcion", menu = filemenu)



# Barra de Captura de los datos
buscar_entry = Entry(textvariable=buscar, width=50)
buscar_entry.place(x=50, y=100)


# Funcion para el buscador
def Buscador():
    buscar_data = buscar.get()
    result = Listbox(ventana, width = 85, height= 20)
    result.place(x = 40, y = 130)

    for i in search(buscar_data, num_results = 20, lang = 'es'):
        print(i)
        result.insert(0, i)



# creando boton
btnBuscar = Button(ventana, text="Buscar", font = ("Cambria", 12), command = Buscador, width = "10", fg = "white",
                   height = "1", bg="#24b43c")
btnBuscar.place(x=400, y=95)

if __name__ == '__main__':
    ventana.mainloop()
