from flask import Blueprint, request, jsonify
from app.services.face_recognition_service import verify_identity

student_controller = Blueprint('student_controller', __name__)

@student_controller.route('/verify_identity', methods=['POST'])
def verify_identity_route():
    image = request.files['image']
    student_id = request.form['student_id']
    result = verify_identity(image, student_id)
    return jsonify(result)
