from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import Episode, Appearance, db

def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': ep.id,
        'date': ep.date.isoformat(),
        'number': ep.number
    } for ep in episodes]), 200

def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [{
        'id': app.id,
        'rating': app.rating,
        'guest': {
            'id': app.guest.id,
            'name': app.guest.name,
            'occupation': app.guest.occupation
        }
    } for app in episode.appearances]
    
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }), 200

@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200