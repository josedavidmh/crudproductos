from flask import Blueprint
from flasgger import swag_from
from app.common import error_bp
from app.services import product_add,product_delete,product_detail
from app.services import product_list,product_update

productos_bp = Blueprint('productos', __name__)

@swag_from({
    'summary':'Consulta general de productos',
    'responses': {
        200: {'description': 'Información general de productos'},
        400: {'description':'Error en la consulta'}
    } 
    })
@productos_bp.route("/products")
def get_product_list():
    productos = product_list()
    return productos

@swag_from({
    'summary':'Consulta individual de productos',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID del producto consultar',
            'example': 1
        }
        ],
    'responses': {
        200: {'description': 'Información individual de productos'},
        400: {'description':'Error en la consulta'}
    } 
    })    
@productos_bp.route("/products/<int:id>")
def get_product_detail(id):
    producto = product_detail(id)
    return producto

@swag_from({
    'summary':'Registro de productos',
    'description':'Crea un nuevo producto en la base de datos',
    'parameters': [
        {
            'name':'body',
            'in': 'body',
            'required':True,
            'schema':{
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string', 'example':'Manzana'},
                    'descripcion':{'type':'string', 'example':'Manzana Chilena'},
                    'precio': {'type': 'number', 'format':'float', 'example': 10.5}
                }
            }
    }],
    'responses': {
        201: {'description': 'producto agregado exitosamente',
            'examples':{
                'application/json': {'mensaje': 'Registro agregado exitosamente'} 
                        }
            },
        400: {'description':'Error en el registro',
            'examples':{
                'application/json': {'mensaje': 'Error', 'descripcion': 'detalle del error'} 
                        }
            }
    } 
    })    
@productos_bp.route("/products",methods=["POST"])
def get_product_add():
    producto = product_add()
    return producto

@swag_from({
    'summary':'Actualización de productos',
    'description':'Actualiza los productos por ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID del producto  actualizar',
            'example': 1
        },
        {
            'name':'body',
            'in': 'body',
            'required':True,
            'schema':{
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string', 'example':'Manzana'},
                    'descripcion':{'type':'string', 'example':'Manzana Chilena'},
                    'precio': {'type': 'number', 'format':'float', 'example': 10.5}
                }
            }
    }],
    'responses': {
        200: {'description': 'producto actualizado exitosamente',
            'examples':{
                'application/json': {'mensaje': 'Registro actualizado exitosamente'} 
                        }
            },
        400: {'description':'Error en el registro',
            'examples':{
                'application/json': {'mensaje': 'Error', 'descripcion': 'detalle del error'} 
                        }
            }
    } 
    })
@productos_bp.route("/products/<int:id>",methods=["PUT"])
def get_product_update(id):
    producto = product_update(id)
    return producto
    
@swag_from({
    'summary':'Eliminación de productos',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID del producto eliminar',
            'example': 1
        }
        ],
    'responses': {
        200: {'description': 'Producto eliminado exitosamente'},
        400: {'description':'Error en la eliminación',
        'examples':{
                'application/json':{'mensajes': 'Error', 'descripcion': 'detalle del error'}
            }
        }
    } 
    }) 
@productos_bp.route("/products/<int:id>",methods=['DELETE'])
def get_product_delete(id):
    producto = product_delete(id)
    return producto