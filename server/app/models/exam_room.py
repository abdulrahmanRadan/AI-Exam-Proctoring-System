from app import db

class ExamRoom(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(100))
    allocated_students = db.Column(db.String(100))
    monitors = db.Column(db.String(100))

    def save(self):
        db.session.add(self)
        db.session.commit()
