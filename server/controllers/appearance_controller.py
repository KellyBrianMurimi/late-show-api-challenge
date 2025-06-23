from flask import request, jsonify
from flask_jwt_extended import jwt_required
from server.models import Appearance, db

@jwt_required()
def create_appearance():
    data = request.get_json()
    
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not all([rating, guest_id, episode_id]):
        return jsonify({'error': 'Missing required fields'}), 400

    if not (1 <= int(rating) <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201