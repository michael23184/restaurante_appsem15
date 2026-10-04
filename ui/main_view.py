import tkinter as tk
from tkinter import messagebox

class MainView:
    def __init__(self, root, usuario):
        self.root = root
        self.root.title("Restaurante App - Principal")
        self.root.geometry("600x400")
        self.root.configure(bg="#ffffff")

        # Encabezado con bienvenida
        tk.Label(root, text=f"Bienvenido {usuario.nombre}",
                 font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=20)

        # Menú principal con botones
        tk.Button(root, text="Gestión de Productos",
                  command=self.gestion_productos,
                  bg="#2196F3", fg="white", width=25, height=2).pack(pady=10)

        tk.Button(root, text="Gestión de Ventas",
                  command=self.gestion_ventas,
                  bg="#4CAF50", fg="white", width=25, height=2).pack(pady=10)

        tk.Button(root, text="Reportes",
                  command=self.reportes,
                  bg="#FF9800", fg="white", width=25, height=2).pack(pady=10)

        tk.Button(root, text="Salir",
                  command=self.root.quit,
                  bg="#f44336", fg="white", width=25, height=2).pack(pady=20)

    def gestion_productos(self):
        messagebox.showinfo("Gestión de Productos", "Aquí irá la gestión de productos.")

    def gestion_ventas(self):
        messagebox.showinfo("Gestión de Ventas", "Aquí irá la gestión de ventas.")

    def reportes(self):
        messagebox.showinfo("Reportes", "Aquí irá la generación de reportes.")

# Para pruebas rápidas
if __name__ == "__main__":
    root = tk.Tk()
    # Simulación de usuario
    class Usuario:
        def __init__(self, nombre):
            self.nombre = nombre
    usuario_demo = Usuario("Michael")
    app = MainView(root, usuario_demo)
    root.mainloop()