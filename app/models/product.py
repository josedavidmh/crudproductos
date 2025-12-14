from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

class Base (DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Product(db.Model):
    id : Mapped[int] = mapped_column (primary_key=True)
    nombre: Mapped[str]= mapped_column(String(50),unique=True)
    descripcion: Mapped[str]= mapped_column(String(100))
    precio: Mapped[float] = mapped_column(DECIMAL(10,2))
    
    def to_dict(self):
        return{
            "id":self.id,
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "precio": self.precio
        }


