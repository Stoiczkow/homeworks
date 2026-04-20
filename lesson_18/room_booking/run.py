from app import create_app, db
from app.models import User, Equipment, Room, Booking

app = create_app()


def seed_data():
    if User.query.first():
        print("Dane już istnieją.")
        return

    projektor = Equipment(name="Projektor", icon="projector")
    tablica = Equipment(name="Tablica", icon="whiteboard")
    wideokonferencja = Equipment(name="Wideokonferencja", icon="video")

    sala_a1 = Room(
        name="Sala A1",
        capacity=10,
        floor=1,
        description="Mała sala do spotkań",
        hourly_rate=50,
    )

    sala_b2 = Room(
        name="Sala B2",
        capacity=20,
        floor=2,
        description="Średnia sala z projektorem",
        hourly_rate=80,
    )

    sala_a1.equipment = [tablica]
    sala_b2.equipment = [projektor, wideokonferencja]

    jan = User(
        email="jan@firma.pl",
        name="Jan Kowalski",
        department="IT",
    )

    anna = User(
        email="anna@firma.pl",
        name="Anna Nowak",
        department="HR",
    )

    db.session.add_all([
        projektor,
        tablica,
        wideokonferencja,
        sala_a1,
        sala_b2,
        jan,
        anna,
    ])
    db.session.commit()
    print("Dodano dane testowe.")


@app.route("/")
def index():
    return "Flask działa!"


@app.route("/test-db")
def test_db():
    try:
        db.session.execute(db.text("SELECT 1"))
        return "Połączenie z PostgreSQL OK!"
    except Exception as e:
        return f"Błąd połączenia: {str(e)}"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
        print("Tabele utworzone!")

    app.run(debug=True)