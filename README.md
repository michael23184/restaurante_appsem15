# Restaurante App - Semana 15

Aplicativo desarrollado en Python como parte de la asignatura de **Programación Orientada a Objetos (POO)**.  
El sistema permite gestionar usuarios, productos, ventas y reportes dentro de un entorno académico, con interfaz gráfica en **Tkinter**.

---

## 📂 Estructura del proyecto

restaurante_appsem15/
│
├── datos/
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
│
├── servicios/
│   ├── auth_service.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   └── logo.png.png
│
├── main.py
├── README.md
└── .gitignore

Código

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Librerías:
  - `tkinter` (incluida en Python)
  - `pillow` (para manejo de imágenes)

Instalación de dependencias:
```bash
pip install pillow
🚀 Ejecución
Clonar el repositorio:

bash
git clone <URL-del-repositorio>
cd restaurante_appsem15
Ejecutar el programa:

bash
python main.py
Se abrirá la ventana de Login.
Ingresa un usuario válido desde datos/usuarios.json.

👥 Usuarios de prueba
Ejemplo de usuarios disponibles en usuarios.json:

json
[
    {
        "identificacion": "U001",
        "nombre": "Michael",
        "correo": "michael@correo.com",
        "clave": "1234"
    },
    {
        "identificacion": "U002",
        "nombre": "Ana",
        "correo": "ana@correo.com",
        "clave": "4321"
    },
    {
        "identificacion": "U005",
        "nombre": "Docente",
        "correo": "docente@universidad.com",
        "clave": "evaluar"
    }
]
🖥️ Flujo del sistema
Login

Validación por correo y clave.

Mensaje de bienvenida si el acceso es correcto.

Ventana principal (main_view.py)

Menú con botones:

Gestión de Productos

Gestión de Ventas

Reportes

Salir

Gestión de datos

Los archivos JSON (usuarios.json, ventas.json) almacenan la información.

Se accede mediante los servicios (auth_service.py, archivo_servicio.py).

🎨 Interfaz
Logo redimensionado (100x100 px).

Colores diferenciados en botones.

Contraste mejorado para etiquetas y campos.

✅ Checklist de validación
[x] Login funcional con varios usuarios.

[x] Logo visible y redimensionado.

[x] Botón “Ingresar” accesible.

[x] Ventana principal con menú.

[x] Repositorio limpio y organizado.

📌 Nota académica
Este proyecto corresponde a la Semana 15 de la asignatura de POO.
El objetivo es demostrar la correcta aplicación de fundamentos de programación orientada a objetos, manejo de archivos, modularidad y diseño de interfaz gráfica.