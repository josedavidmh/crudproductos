from app.models import Product, db
from flask import jsonify,request,abort

def product_list():
    productos=Product.query.all()
    ##return jsonify([p.to_dict() for p in productos] ),200
    return [p.to_dict() for p in productos]

def product_detail(id):
    producto=Product.query.get_or_404(id)
    ##return jsonify(producto.to_dict()),200
    return producto.to_dict()

def product_add(nombre, descripcion, precio):
    # 422 Unprocessable Entity (Entidad no procesable) 
    if type(precio) not in (int,float) or precio<=0:
        abort(422,"El precio debe ser un número mayor a cero (0)")
        
    nuevo_producto=Product(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio    
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return nuevo_producto
    
def product_update(id, nombre, descripcion, precio):       
    # 422 Unprocessable Entity (Entidad no procesable) 
    if type(precio) not in (int,float) or precio<=0:
        abort(422,"El precio debe ser un número mayor a cero (0)")
    
    producto=Product.query.get_or_404(id)
    if nombre is not None:
        producto.nombre=nombre
    if descripcion is not None:
        producto.descripcion=descripcion
    if precio is not None:
        producto.precio=precio
    db.session.commit()
    return producto
    
def product_delete(id):
    producto=Product.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return "Producto eliminado exitosamente"
