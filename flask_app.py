from flask import Flask, jsonify, request 
app = Flask(__name__)

# Datos simulados
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 20},
    {"id": 2, "nombre": "Pantalón", "precio": 35},
    {"id": 3, "nombre": "Zapatos", "precio": 50}
]

carrito = []

@app.route('/')
def index():
    return jsonify(productos)

@app.route('/agregar/<int:id>', methods=['POST'])
def agregar(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto:
        carrito.append(producto)
        return jsonify({"mensaje": "Producto agregado", "carrito": carrito})
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@app.route('/carrito')
def ver_carrito():
    total = sum(p["precio"] for p in carrito)
    return jsonify({"carrito": carrito, "total": total})

if __name__ == '__main__':
    app.run(debug=True)
