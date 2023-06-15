import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Menu

def salir():
    ventana_inicial.destroy()
    
def manual_usuario():
    messagebox.showinfo("Manual de usuario", "En construcción...")

def acerca_de():
    messagebox.showinfo("Acerca de...", "Versión 1.0")
  
def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    # Validación del campo de usuario
    if not usuario.isdigit():
        lbl_mensaje.config(text="El usuario debe contener solo números.")
        return
    
    # Ejemplo básico de autenticación
    if usuario == "2214079" and contrasena == "p":
        ventana_inicial.destroy()
        abrir_ventana_principal()
    elif usuario != "2214079":
        lbl_mensaje.config(text="El usuario es incorrecto.")
    elif contrasena != "p":
        lbl_mensaje.config(text="La contraseña es incorrecta.")

def abrir_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Bienvenido a UIS Bike Rental")
    ventana_principal.geometry("400x300")
    barra_menus = Menu()
    ventana_principal.config(menu=barra_menus)
    menu_edicion = Menu(tearoff=0)
    ventana_principal.resizable(0,0)
    barra_menus = Menu()

    

    lbl_bienvenido = tk.Label(ventana_principal, text="¡Bienvenido a UIS Bike Rental!",font=("Times New Roman",16),bg="#19CCAE")
    lbl_bienvenido.pack(pady=20)
    lbl_definicion = tk.Label(ventana_principal, text="Esta es una aplicación que muestra diversos precios\n disponibles de renta desde el menor a mayor, de momento y \nque tenga un buen rango de confiabilidad, buscándose \nuna aplicación para tu cuidado.")
    lbl_definicion.pack(pady=40)

    btn_siguiente = ttk.Button(ventana_principal, text="Siguiente", command=lambda: abrir_ventana_datos(ventana_principal))
    btn_siguiente.pack(side="bottom", pady=20, padx=10, anchor="se")

def abrir_ventana_datos(ventana_anterior):
    ventana_anterior.destroy()

    ventana_datos = tk.Tk()
    ventana_datos.title("Ingresar datos")
    ventana_datos.geometry("400x400")
    barra_menus = Menu()
    ventana_datos.config(menu=barra_menus)
    menu_edicion = Menu(tearoff=0)
    ventana_datos.resizable(0,0)

    style = ttk.Style()
    style.theme_use("clam")

    lbl_nombre = tk.Label(ventana_datos, text="Nombre:")
    lbl_nombre.pack()
    entry_nombre = ttk.Entry(ventana_datos)
    entry_nombre.pack()

    lbl_edad = tk.Label(ventana_datos, text="Edad:")
    lbl_edad.pack()
    entry_edad = ttk.Entry(ventana_datos)
    entry_edad.pack()

    lbl_carrera = tk.Label(ventana_datos, text="Carrera:")
    lbl_carrera.pack()
    entry_carrera = ttk.Entry(ventana_datos)
    entry_carrera.pack()

    lbl_tiempo = tk.Label(ventana_datos, text="Tiempo por el cual va a tener la cicla:")
    lbl_tiempo.pack()
    entry_tiempo = ttk.Entry(ventana_datos)
    entry_tiempo.pack()

    lbl_renta_cicla = tk.Label(ventana_datos, text="¿Desea aplicar para la renta de cicla?")
    lbl_renta_cicla.pack()
    opciones_renta_cicla = ["Sí", "No"]
    seleccion_multiple = tk.StringVar(ventana_datos, value=opciones_renta_cicla[0])
    dropdown = ttk.OptionMenu(ventana_datos, seleccion_multiple, *opciones_renta_cicla)
    dropdown.pack()

    lbl_sede = tk.Label(ventana_datos, text="Sede:")
    lbl_sede.pack()
    opciones_sede = ["Malaga", "Barbosa", "Socorro", "Barrancabermeja", "Sede Central"]
    seleccion_sede = tk.StringVar(ventana_datos, value=opciones_sede[0])
    dropdown_sede = tk.OptionMenu(ventana_datos, seleccion_sede, *opciones_sede)
    dropdown_sede.pack()
    entry_sede = ttk.Entry(ventana_datos)
    entry_sede.pack()


    def guardar_datos():
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        carrera = entry_carrera.get()
        sede = entry_sede.get()
        tiempo = entry_tiempo.get()
        opcion_seleccionada = seleccion_multiple.get()

        # Mostrar la información en una ventana emergente
        mensaje = f"Nombre: {nombre}\nEdad: {edad}\nSede: {carrera}\nTiempo: {tiempo}\nOpción seleccionada: {opcion_seleccionada}\n{sede}"
        messagebox.showinfo("Información guardada", mensaje)

        ventana_datos.destroy()

    btn_guardar = ttk.Button(ventana_datos, text="Guardar", command=guardar_datos)
    btn_guardar.pack(pady=20)

    ventana_datos.mainloop()

def abrir_ventana_base_datos():
    ventana_bd = tk.Toplevel()
    ventana_bd.title("Requiere Base de Datos")
    ventana_bd.geometry("400x400")
    barra_menus = Menu()
    abrir_ventana_base_datos.config(menu=barra_menus)
    menu_edicion = Menu(tearoff=0)
    abrir_ventana_base_datos.resizable(0,0)

    lbl_mensaje_bd = tk.Label(ventana_bd, text="Se requiere una base de datos para esta funcionalidad.")
    lbl_mensaje_bd.pack(pady=20)

    ventana_bd.mainloop()

ventana_inicial = tk.Tk()
ventana_inicial.title("UIS BIKE RENTAL ")
ventana_inicial.geometry("300x200")
barra_menus = Menu()
ventana_inicial.config(menu=barra_menus)
menu_edicion = Menu(tearoff=0)
ventana_inicial.resizable(0,0)

style = ttk.Style()
style.theme_use("clam")

lbl_usuario = tk.Label(ventana_inicial, text="Usuario:")
lbl_usuario.pack()
entry_usuario = ttk.Entry(ventana_inicial)
entry_usuario.pack()

lbl_contrasena = tk.Label(ventana_inicial, text="Contraseña:")
lbl_contrasena.pack()
entry_contrasena = ttk.Entry(ventana_inicial, show="*")
entry_contrasena.pack()

lbl_mensaje = tk.Label(ventana_inicial, text="")
lbl_mensaje.pack()

lbl_olvidaste_contrasena = tk.Label(ventana_inicial, text="¿Olvidaste tu contraseña?", fg="blue", cursor="hand2")
lbl_olvidaste_contrasena.pack(pady=10)

def cambiar_color(event):
    lbl_olvidaste_contrasena.config(fg="red")

def restaurar_color(event):
    lbl_olvidaste_contrasena.config(fg="blue")

lbl_olvidaste_contrasena.bind("<Enter>", cambiar_color)
lbl_olvidaste_contrasena.bind("<Leave>", restaurar_color)
lbl_olvidaste_contrasena.bind("<Button-1>", lambda event: abrir_ventana_base_datos())

btn_iniciar_sesion = ttk.Button(ventana_inicial, text="Iniciar sesión", command=iniciar_sesion)
btn_iniciar_sesion.pack()

# BARRA DE MENU 
menu_archivo = Menu(tearoff=0)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", compound="left", command=salir)
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)
menu_edicion.add_command(label="En proceso ", command=manual_usuario)
barra_menus.add_cascade(label="Edición", menu=menu_edicion)
menu_ayuda = Menu(tearoff=0)
menu_ayuda.add_command(label="Términos y Condiciones", command=manual_usuario)
menu_ayuda.add_command(label="Versión del programa", command=acerca_de)
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana_inicial.mainloop()
