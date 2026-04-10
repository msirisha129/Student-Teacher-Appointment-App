from flask import Blueprint, request, jsonify
from models import db, TeacherAvailability, Appointment

teacher = Blueprint("teacher", __name__)

@teacher.route("/add-availability", methods=["POST"])
def add_availability():
    data = request.json

    slot = TeacherAvailability(
        teacher_id=data["teacher_id"],
        date=data["date"],
        time=data["time"]
    )

    db.session.add(slot)
    db.session.commit()

    return jsonify({"message": "Availability added"})


@teacher.route("/appointments/<int:teacher_id>")
def view_requests(teacher_id):
    appointments = Appointment.query.filter_by(teacher_id=teacher_id).all()

    result = []
    for a in appointments:
        result.append({
            "id": a.id,
            "student_id": a.student_id,
            "date": a.date,
            "time": a.time,
            "status": a.status
        })

    return jsonify(result)


@teacher.route("/update-status", methods=["POST"])
def update_status():
    data = request.json
    appointment = Appointment.query.get(data["appointment_id"])

    appointment.status = data["status"]
    appointment.remarks = data.get("remarks", "")

    db.session.commit()

    return jsonify({"message": "Status updated"})