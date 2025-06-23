from flask import jsonify
from server.models import Guest

def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    } for guest in guests]), 200