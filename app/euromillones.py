from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, db
import asyncio
from scraper import get_euromillones

euromillones_bp = Blueprint('euromillones', __name__)

@euromillones_bp.route('/euromillones', methods=['GET'])
@jwt_required()
def euromillones():
    email = get_jwt_identity()
    user = User.query.get(email)
    if user.requests_left <= 0:
        return jsonify({"error": "Request limit reached"}), 403

    fecha = request.args.get('date')
    if not fecha:
        return jsonify({"error": "'fecha' parameter is required"}), 400

    resultados = asyncio.run(get_euromillones(fecha))
    if resultados is None:
        return jsonify({"error": "No results found for that date"}), 404

    user.requests_left -= 1
    db.session.commit()

    return jsonify(resultados)
