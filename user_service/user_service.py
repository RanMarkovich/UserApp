from flask import Flask, request, jsonify

from data.data_validator import DataValidator
from database.database import Database

app = Flask(__name__)
db = Database()
validator = DataValidator()


@app.route('/register', methods=['POST'])
def register():
    user = request.get_json()
    validation = validator.validate_user_payload(user)
    if not validation[0]:
        return jsonify({'error': {'code': 400, 'message': validation[1].message}}), 400
    first_name = user['firstName']
    last_name = user['lastName']
    user_name = user['userName']
    email = user['email']
    password = user['password']
    if not db.is_email_exit(email):
        db.create_user(first_name, last_name, user_name, email, password)
        return jsonify(sucess=True), 200
    else:
        return jsonify(sucess=False), 409


@app.route('/login', methods=['POST'])
def login():
    login_ = request.get_json()
    email = login_['email']
    password = login_['password']
    if db.validate_user(email, password):
        return jsonify(sucess=True), 200
    else:
        return jsonify(sucess=False), 400


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
