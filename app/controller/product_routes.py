from flask import Blueprint
from flasgger import swag_from
from app.services import product_add,product_delete,product_detail
from app.services import product_list,product_update
from flask import Flask, request, jsonify
# Importaciones de Ariadne para trabajar con GraphQL
# QueryType y MutationType permiten definir resolvers para consultas y mutaciones
# make_executable_schema crea el esquema ejecutable de GraphQL
from ariadne import QueryType, MutationType, make_executable_schema
# ExplorerGraphiQL proporciona la interfaz visual para probar consultas GraphQL
from ariadne.explorer import ExplorerGraphiQL
# graphql_sync ejecuta las consultas GraphQL de forma síncrona
from ariadne.graphql import graphql_sync

productos_bp = Blueprint('productos', __name__)

# Definición del esquema GraphQL (typeDefs)
# Se definen los tipos, consultas (Query) y mutaciones (Mutation)
type_defs = """
    # Tipo Producto con sus atributos
    type Producto {
        id: Int!
        nombre: String!
        descripcion: String!
        precio: Float!
    }

    # Consultas disponibles en la API GraphQL
    type Query {
        listarProductos: [Producto!]!
        productoPorId(id: Int!): Producto
    }

    # Mutaciones disponibles para modificar datos
    type Mutation {
        crearProducto(nombre: String!, descripcion: String!, precio: Float!): Producto
        modificarProducto(id: Int!, nombre: String, descripcion: String, precio: Float): Producto
        eliminarProducto(id: Int!): String
    }
"""
# Resolvers de las consultas (Query)
query = QueryType()

# Resolver para listar todos los productos
@query.field("listarProductos")
def resolve_listar_productos(_, info):
    productos = product_list()
    return productos

# Resolver para consultar un producto por su ID
@query.field("productoPorId")
def resolve_producto_por_id(_, info, id):
    producto = product_detail(id)
    return producto

# Resolvers de las mutaciones (Mutation)
mutation = MutationType()

# Resolver para crear un nuevo producto
@mutation.field("crearProducto")
def resolve_crear_producto(_, info, nombre, descripcion, precio):
    try:
        return product_add(nombre, descripcion, precio)
    except Exception as e:
        raise Exception(str(e))
    
@mutation.field("modificarProducto")
def resolve_modificar_producto(_, info, id, nombre=None, descripcion=None, precio=None):
    try:
        return product_update(id, nombre, descripcion, precio)
    except Exception as e:
        raise Exception(str(e))

@mutation.field("eliminarProducto")
def resolve_eliminar_producto(_, info, id):
    return product_delete(id)
    
# Creación del esquema ejecutable de GraphQL
schema = make_executable_schema(type_defs, query, mutation)

# Endpoint único de GraphQL
# Maneja tanto consultas (GET) como ejecuciones (POST)
@productos_bp.route("/graphql", methods=["GET", "POST"])
def graphql_server():
    # Si se accede por GET, se muestra la interfaz GraphiQL
    if request.method == "GET":
        return ExplorerGraphiQL().html(request)

    # Si se accede por POST, se ejecuta la consulta GraphQL
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=True
    )
    # Se retorna la respuesta en formato JSON
    return jsonify(result), 200 if success else 400
    