# Sistema de gestión de inventario

Un sistema de gestión de inventario ligero y seguro desarrollado en Python con Flask. El proyecto evolucionó de ser un script de consola a una aplicación web completa con interfaz gráfica, autenticación de usuarios y filtrado en tiempo real.

## Características a destacar:

* **Interfaz de Usuario (UI):** Diseño oscuro responsivo utilizando HTML, CSS personalizado y Bootstrap.
* **Autenticación Segura:** Sistema de Login y Registro de usuarios. Las contraseñas se almacenan encriptadas para mayor seguridad.
* **Gestión de Sesiones:** Rutas protegidas que impiden el acceso a usuarios no autorizados.
* **CRUD de Inventario:** Permite visualizar, añadir y eliminar productos de la base de datos de forma intuitiva.
* **Búsqueda en Tiempo Real:** Filtrado dinámico de productos en el lado del cliente sin necesidad de recargar la página.
* **Persistencia de Datos:** Almacenamiento local mediante SQLite3.

## Herramientas/tecnologías utilizadas:

* **Backend:** Python 3.11, Flask
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (Vanilla)
* **Base de Datos:** SQLite3
* **Seguridad:** Werkzeug (Password Hashing), variables de entorno (`python-dotenv`)

## Estructura del Proyecto

Gestión_inventario/
├── data/
│   └── inventario.db         # Base de datos SQLite
├── src/
│   ├── static/
│   │   └── style.css         # Estilos personalizados
│   ├── templates/
│   │   ├── index.html        # Panel principal del inventario
│   │   └── login.html        # Pantalla de inicio de sesión
│   ├── app.py                # Servidor y rutas de Flask
│   ├── database.py           # Lógica y conexión a la base de datos
│   └── verify.py             # Validaciones de entrada de datos
├── .env.example              # Plantilla para variables de entorno
├── .gitignore                # Archivos ignorados por Git
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto