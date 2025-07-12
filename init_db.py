from ext import app, db
from models import Movie, User

with app.app_context():
    db.drop_all()
    db.create_all()

    admin_user = User(email="admin@gmail.com", password="admin123", role="admin")
    db.session.add(admin_user)
    db.session.commit()
