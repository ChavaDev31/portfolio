from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, esta es mi primera API con Flask!"

@app.route('/info')
def info():
    data = {
        "nombre": "Mi API",
        "version": "1.0",
        "autor": "Salvador"
    }

    return jsonify(data)

@app.route('/datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    datos["procesando"] = True
    
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)


