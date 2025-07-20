from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, db 
import asyncio
from scrapper.scraper import get_euromillones
from storage import save_result, get_result_by_date
import json

euromillones_bp = Blueprint('euromillones', __name__)

@euromillones_bp.route('/euromillones', methods=['GET'])
@jwt_required()
def euromillones():
    email = get_jwt_identity()
    user = User.query.get(email)
    if user.requests_left <= 0:
        return jsonify({"error": "Request limit reached"}), 403

    date = request.args.get('date')
    
    if not date:
        return jsonify({"error": "'date' parameter is required"}), 400
    result = get_result_by_date(date)
    
    if result:
        user.requests_left -= 1
        db.session.commit()
        return {
            "date": result.date,
            "numbers": [int(n) for n in result.numbers.split(',')],
            "stars": [int(s) for s in result.stars.split(',')],
            "prizes": json.loads(result.prizes) 
        }

    result = asyncio.run(get_euromillones(date))
    if result is None:
        return jsonify({"error": "No results found for that date"}), 404

    save_result(date,result['numbers'],result['stars'], result['prices'])
    
    user.requests_left -= 1
    db.session.commit()

    return jsonify(result)
