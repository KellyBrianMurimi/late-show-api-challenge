import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from server.app import app
from server.extensions import db
from server.models import User, Guest, Episode, Appearance
from datetime import date

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        user = User(username='admin')
        user.set_password('password123')
        db.session.add(user)
        
        guest1 = Guest(name='John Doe', occupation='Actor')
        guest2 = Guest(name='Jane Smith', occupation='Musician')
        db.session.add_all([guest1, guest2])
        
        episode1 = Episode(date=date(2023, 1, 1), number=101)
        episode2 = Episode(date=date(2023, 1, 2), number=102)
        db.session.add_all([episode1, episode2])
        
        appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
        appearance2 = Appearance(rating=5, guest_id=2, episode_id=2)
        db.session.add_all([appearance1, appearance2])
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()