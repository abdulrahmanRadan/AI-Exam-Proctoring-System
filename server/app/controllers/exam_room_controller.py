from flask import Blueprint, request, jsonify
from app.models.exam_room import ExamRoom

exam_room_controller = Blueprint('exam_room_controller', __name__)

@exam_room_controller.route('/allocate_room', methods=['POST'])
def allocate_room():
    data = request.get_json()
    room = ExamRoom(**data)
    room.save()
    return jsonify({"status": "success", "message": "Room allocated successfully"})
