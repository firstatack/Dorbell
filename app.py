from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Ruta para la página principal (HTML)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la acción de presionar el timbre
@app.route('/doorbell', methods=['POST'])
def doorbell():
    # Datos del request (enviar con JSON)
    headers = {
        'Authorization': 'Bearer SUSTITUIR POR EL TOKEN',  #############INTRODUCIR TOKEN######
        'Content-Type': 'application/json',
    }

    # Datos del timbre (acción)
    data = {
        "type": "event",
        "action": "DoorbellPress",
        "value": json.dumps({"state": "pressed"})
    }

    # Hacer la solicitud POST a Sinric Pro
    #COMPLETA LA URL CON TU DATOS DEVICE_ID Y CLIENT_ID Y API_KEY

    url = "https://api.sinric.pro/api/v1/devices/DEVICE_ID/action?clientId=CLIENT_ID&messageId=API_KEY&type=event&action=DoorbellPress&createdAt=1739217360&value=%7B%22state%22:%22pressed%22%7D"
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        return jsonify({"status": "success", "message": "Timbre activado correctamente."}), 200
    else:
        return jsonify({"status": "error", "message": "Hubo un error al activar el timbre."}), 500

if __name__ == '__main__':
    app.run(debug=True)
