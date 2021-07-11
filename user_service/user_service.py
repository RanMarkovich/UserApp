from flask import Flask, request, jsonify

from database.database import Database

app = Flask(__name__)
db = Database()


@app.route('/register', methods=['POST'])
def register():
    user = request.get_json()
    first_name = user['firstName']
    last_name = user['lastName']
    user_name = user['userName']
    email = user['email']
    password = user['password']
    db.create_user(first_name, last_name, user_name, email, password)
    return jsonify(sucess=True), 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
