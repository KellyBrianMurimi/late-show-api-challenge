from flask import request, jsonify
from flask_jwt_extended import jwt_required
from ..models import db, Appearance, Guest, Episode
from ..controllers import api

@api.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    
    # Verify guest and episode exist
    if not Guest.query.get(data['guest_id']):
        return jsonify({"message": "Guest not found"}), 404
    if not Episode.query.get(data['episode_id']):
        return jsonify({"message": "Episode not found"}), 404
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201