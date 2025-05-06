# bot.py
from flask import Flask, request
import requests
import json
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Base de conocimiento de la organización estudiantil
knowledge_base = {
    "horario": "El horario de atención es de lunes a viernes de 9:00 a 18:00.",
    "inscripción": "Para inscribirte a la organización, debes completar el formulario en nuestra página web y pagar la cuota anual de $20.",
    "eventos": "Tenemos eventos mensuales, el próximo será el día 15. Consulta el calendario en nuestra página web.",
    "beneficios": "Los miembros de la organización tienen acceso a talleres gratuitos, descuentos en tiendas asociadas y asesoría académica.",
    "contacto": "Puedes contactarnos al correo organizacion@estudiantes.edu o al teléfono 555-123-4567.",
    "ubicación": "Nuestra oficina está ubicada en el edificio central del campus, salón 302.",
    "requisitos": "Para ser miembro debes ser estudiante activo y mantener un promedio mínimo de 7.5.",
    "cuotas": "La cuota anual es de $20, se puede pagar en efectivo o transferencia."
}

def find_answer(message):
    """Busca palabras clave en el mensaje y devuelve la respuesta adecuada"""
    message = message.lower()
    
    # Buscar palabras clave en el mensaje
    for keyword, answer in knowledge_base.items():
        if keyword in message:
            return answer
    
    # Respuesta por defecto
    return "No tengo información sobre esa consulta. ¿Podrías preguntar sobre horarios, inscripción, eventos, beneficios, contacto, ubicación, requisitos o cuotas?"

@app.route('/bot', methods=['POST'])
def bot():
    # Obtener el mensaje entrante
    incoming_msg = request.values.get('Body', '').lower()
    
    # Crear respuesta
    resp = MessagingResponse()
    msg = resp.message()
    
    # Solo responder si el mensaje comienza con '!'
    if incoming_msg.startswith('!'):
        query = incoming_msg[1:].strip()
        response = find_answer(query)
        msg.body(response)
    
    return str(resp)

# Para ejecutar localmente en desarrollo
if __name__ == '__main__':
    app.run(debug=True)