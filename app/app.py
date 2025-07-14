from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from models import db
from auth import auth_bp
from euromillones import euromillones_bp
from datetime import timedelta
#from google_sheets_logger import log_error

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-key'  # Change this in production!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp)
app.register_blueprint(euromillones_bp)

@app.errorhandler(Exception)
def handle_exception(e):
    path = request.path
    error_text = str(e)
    print(error_text)
    #log_error(path, error_text)
    return jsonify({"error": "Internal server error"}), 500

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        "msg": "Token expired. Please request a new one at /auth"
    }), 401

if __name__ == '__main__':
    app.run(debug=True)
