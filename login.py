from conexion import *
import tkinter as tk 
from tkinter import messagebox

#creamos un cursor para interactuar con la bd
cursor = conn.cursor()

ventana = tk.Tk()
ventana.title("CRUD PYTHON")
ventana.geometry("640x480")

lblNombre = tk.Label(text="Nombre:")
lblNombre.grid(row=0, column=0)
entryNombre = tk.Entry()
entryNombre.grid(row=0, column=1)


lblUsuario = tk.Label(text="Usuario")
lblUsuario.grid(row=1,column=0)
entryUsuario = tk.Entry()
entryUsuario.grid(row=1, column=1)

lblPassword = tk.Label(text="Password:")
lblPassword.grid(row=2, column=0)

entryPassword = tk.Entry(show='*')
entryPassword.grid(row=2, column=1)

def registrar():
    try:
        usuario = entryUsuario.get()
        nombre = entryNombre.get()
        clave = entryPassword.get()
        sql = "INSERT INTO user(name,username, password) VALUES(%s,%s,%s)"
        cursor.execute(sql,(nombre,usuario,clave))
        messagebox.showinfo("Alta de usuario", "Registro exitoso")
        
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("Login","Error al conectar a la base de datos")

btnLogin = tk.Button(text="Log in", command=registrar)
btnLogin.grid(row=3, column=0)


ventana.mainloop()
