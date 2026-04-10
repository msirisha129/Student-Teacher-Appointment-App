from flask import Blueprint, request, jsonify
from models import db, Appointment, TeacherAvailability

student = Blueprint("student", __name__)

@student.route("/book", methods=["POST"])
def book_appointment():
    data = request.json

    availability = TeacherAvailability.query.filter_by(
        teacher_id=data["teacher_id"],
        date=data["date"],
        time=data["time"]
    ).first()

    if availability and not availability.is_booked:
        availability.is_booked = True

        appointment = Appointment(
            student_id=data["student_id"],
            teacher_id=data["teacher_id"],
            date=data["date"],
            time=data["time"],
            status="pending"
        )

        db.session.add(appointment)
        db.session.commit()

        return jsonify({"message": "Appointment booked"})

    return jsonify({"error": "Slot not available"}), 400

@student.route("/my-appointments/<int:student_id>")
def get_student_appointments(student_id):
    appointments = Appointment.query.filter_by(student_id=student_id).all()

    result = []
    for a in appointments:
        result.append({
            "id": a.id,
            "date": a.date,
            "time": a.time,
            "status": a.status,
            "remarks": a.remarks
        })

    return jsonify(result)
@student.route("/available-slots")
def available_slots():
    slots = TeacherAvailability.query.filter_by(is_booked=False).all()

    result = []
    for s in slots:
        result.append({
            "id": s.id,
            "date": s.date,
            "time": s.time
        })

    return jsonify(result)