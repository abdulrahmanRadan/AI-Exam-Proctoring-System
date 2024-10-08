from flask import Blueprint, request, jsonify
from app.models.alert import Alert

alert_controller = Blueprint('alert_controller', __name__)

@alert_controller.route('/send_alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    alert = Alert(**data)
    alert.save()
    return jsonify({"status": "success", "message": "Alert sent successfully"})
