from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/exam_proctoring'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# نموذج الطالب
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

@app.route('/')
def index():
    return "AI Exam Proctoring System"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
