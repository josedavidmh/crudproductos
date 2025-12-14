Descripción del proyecto

Backend con servicios API REST para realizar operaciones CRUD sobre una base de datos. 
Framework: Flask 
Entidad Producto con los atributos: id, nombre, descripcion y precio
Base de datos: Mysql

Estructura de carpetas

Backend_rest/
│
│── app/
│   │── models/
│   │   │── __init__.py
│   │   └── product.py              # Modelo
│   │
│   │── services/
│   │   │── __init__.py
│   │   └── product_services.py     # Lógica de negocio
│   │
│   │── controller/
│   │   │── __init__.py
│   │   └── product_routes.py       # Controlador HTTP
│   │
│   │── common/
│   │   └── __init__.py   
│   │   └── config.py               # Archivo de configuración
│   │   └── error.py                # Manejador de errores HTTP            
│── venv/                           # Entorno virtual 
│── main.py                         # Punto de entrada
│── requirements.txt                # Dependencias
│── .gitignore                      # Elementos que no seran cargados al repositorio GitHub
└── README.md

Creación del entorno virtual

# Crear entorno
python -m venv venv

# Activar entorno en Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Habilitar ejecución de scripts en windows
Set-ExecutionPolicy RemoteSigned
# Si se quieres cambiar la política del sistema completo
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

