from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image_data = db.Column(db.LargeBinary)
    allocated_device = db.Column(db.String(100))
    exam_schedule = db.Column(db.String(100))
    exam_room = db.Column(db.String(100))

    def save(self):
        db.session.add(self)
        db.session.commit()
