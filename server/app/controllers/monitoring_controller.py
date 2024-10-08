from flask import Blueprint, request, jsonify
from app.services.monitoring_service import process_monitoring_data

monitoring_controller = Blueprint('monitoring_controller', __name__)

@monitoring_controller.route('/monitor', methods=['POST'])
def monitor():
    data = request.get_json()
    result = process_monitoring_data(data)
    return jsonify(result)
