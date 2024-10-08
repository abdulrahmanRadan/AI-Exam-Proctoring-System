from app import db

class Alert(db.Model):
    alert_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    alert_type = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime)
    details = db.Column(db.String(255))

    def save(self):
        db.session.add(self)
        db.session.commit()
