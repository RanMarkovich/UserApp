from flask import Flask, request, jsonify

from data.data_generator import DataGenerator
from data.data_validator import DataValidator
from database.database import Database

app = Flask(__name__)
db = Database()
validator = DataValidator()
data_generator = DataGenerator()


@app.route('/register', methods=['POST'])
def register():
    user_payload = request.get_json()
    validation = validator.validate_payload(user_payload, data_generator.user_validation_schema())
    if not validation[0]:
        return jsonify({'error': {'code': 400, 'message': validation[1].message}}), 400
    if not db.is_email_exit(user_payload['email']):
        db.create_user(user_payload['firstName'],
                       user_payload['lastName'],
                       user_payload['userName'],
                       user_payload['email'],
                       user_payload['password'])
        return jsonify(sucess=True), 200
    else:
        return jsonify(sucess=False), 409


@app.route('/login', methods=['POST'])
def login():
    login_payload = request.get_json()
    validation = validator.validate_payload(login_payload, data_generator.login_validation_schema())
    if not validation[0]:
        return jsonify({'error': {'code': 400, 'message': validation[1].message}}), 400
    if db.validate_user(login_payload['email'], login_payload['password']):
        return jsonify(sucess=True), 200
    else:
        return jsonify(sucess=False), 400


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
