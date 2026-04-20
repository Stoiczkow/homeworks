from flask import Blueprint, jsonify, request
from app import db
from app.models import Room

rooms_bp = Blueprint("rooms", __name__, url_prefix="/api/rooms")


@rooms_bp.route("/", methods=["GET"])
def get_rooms():
    rooms = Room.query.all()
    return jsonify([room.to_dict() for room in rooms])


@rooms_bp.route("/<int:room_id>", methods=["GET"])
def get_room(room_id):
    room = Room.query.get_or_404(room_id)
    return jsonify(room.to_dict())


@rooms_bp.route("/", methods=["POST"])
def create_room():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Brak danych JSON"}), 400

    required_fields = ["name", "capacity"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Brak wymaganego pola: {field}"}), 400

    if not data["name"].strip():
        return jsonify({"error": "Nazwa sali nie może być pusta"}), 400

    if data["capacity"] < 1:
        return jsonify({"error": "Pojemność musi być większa od 0"}), 400

    if data.get("hourly_rate", 0) < 0:
        return jsonify({"error": "Stawka godzinowa nie może być ujemna"}), 400

    try:
        room = Room(
            name=data["name"],
            capacity=data["capacity"],
            floor=data.get("floor", 0),
            description=data.get("description"),
            hourly_rate=data.get("hourly_rate", 0),
            is_active=data.get("is_active", True),
        )

        db.session.add(room)
        db.session.commit()

        return jsonify({
            "message": "Sala utworzona",
            "room": room.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@rooms_bp.route("/<int:room_id>", methods=["DELETE"])
def delete_room(room_id):
    room = Room.query.get_or_404(room_id)

    try:
        db.session.delete(room)
        db.session.commit()
        return jsonify({"message": f"Sala o ID {room_id} została usunięta"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@rooms_bp.route("/<int:room_id>", methods=["PUT"])
def update_room(room_id):
    room = Room.query.get_or_404(room_id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "Brak danych JSON"}), 400

    try:
        if "name" in data:
            if not data["name"].strip():
                return jsonify({"error": "Nazwa sali nie może być pusta"}), 400
            room.name = data["name"]

        if "capacity" in data:
            if data["capacity"] < 1:
                return jsonify({"error": "Pojemność musi być większa od 0"}), 400
            room.capacity = data["capacity"]

        if "floor" in data:
            room.floor = data["floor"]

        if "description" in data:
            room.description = data["description"]

        if "hourly_rate" in data:
            if data["hourly_rate"] < 0:
                return jsonify({"error": "Stawka godzinowa nie może być ujemna"}), 400
            room.hourly_rate = data["hourly_rate"]

        if "is_active" in data:
            room.is_active = data["is_active"]

        db.session.commit()

        return jsonify({
            "message": "Sala zaktualizowana",
            "room": room.to_dict()
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    