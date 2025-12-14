from app.common import error_bp
from app.models import Product, db
from flask import jsonify,request,abort

def product_list():
    productos=Product.query.all()
    return jsonify([p.to_dict() for p in productos] ),200
    
def product_detail(id):
    producto=Product.query.get_or_404(id)
    return jsonify(producto.to_dict()),200

def product_add():
    data=request.get_json()
    # 400 Bad Request (solicitud incorrecta) 
    if not data:
        abort(400,description="No se recibio información en formato json")
    
    if "nombre" not in data or "precio" not in data:
        abort(400,description="faltan campos obligatorios")
        
    # 422 Unprocessable Entity (Entidad no procesable) 
    if type(data["precio"]) not in (int,float) or data["precio"]<=0:
        #abort(422,"El precio debe ser un número mayor a cero (0)")
        return jsonify({"mensaje":"El precio debe ser un número mayor a cero (0)"}),422
        
    nuevo_producto=Product(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        precio=data['precio']    
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({"mensaje":"producto agregado exitosamente"}),201
    
def product_update(id):
    # 400 Bad Request (solicitud incorrecta)
    data=request.get_json()
    if not data:
        abort(400,description="No se recibio información en formato json")
    
    if "nombre" not in data or "precio" not in data:
        abort(400,description="faltan campos obligatorios")
        
    # 422 Unprocessable Entity (Entidad no procesable)
    if type(data["precio"]) not in (int,float) or data["precio"] <= 0:
        abort(422,"El precio debe ser un número mayor a cero (0)")
        
    producto=Product.query.get_or_404(id)
    producto.nombre=data.get('nombre',producto.nombre)
    producto.descripcion=data.get('descripcion',producto.descripcion)
    producto.precio=data.get('precio',producto.precio)
    db.session.commit()
    return jsonify({"mensaje":"Producto actualizado exitosamente"}),200
    
def product_delete(id):
    producto=Product.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"mensaje":"Producto eliminado exitosamente"}), 200
