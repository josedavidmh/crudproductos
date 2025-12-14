## Con SQLite
class Config:
    SQLALCHEMY_DATABASE_URI="sqlite:///project.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
## Con Mysql
"""import pymysql
class Config:
    # Datos de conexión para MySQL (ajusta según tus credenciales)
    USER = 'root'               # Usuario de MySQL
    PASSWORD = '1234'       # Contraseña de MySQL
    HOST = 'localhost'          # Host donde corre MySQL (localhost por defecto)
    DATABASE = 'db_orm' # Nombre de la base de datos
    
    # URL de conexión para SQLAlchemy usando el conector PyMySQL
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    
    # Desactiva el rastreo de modificaciones para evitar advertencias
    SQLALCHEMY_TRACK_MODIFICATIONS = False"""
