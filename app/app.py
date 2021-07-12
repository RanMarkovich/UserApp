from flask import Flask, render_template, request, jsonify

from data.data_generator import DataGenerator
from services.transport import Transport


app = Flask(__name__)
data = DataGenerator()
transport = Transport()


@app.route('/register', methods=['POST'])
def register():
    user = data.user(request.form['fname'],
                     request.form['lname'],
                     request.form['uname'],
                     request.form['email'],
                     request.form['password'])
    r = transport.register(user)
    if r.status_code == 200:
        return '<p>registered!</p>', 200
    elif r.status_code == 409:
        return f'<p>registration failed! user with email: {user["email"]}, already exist!</p>'
    else:
        return jsonify({'error': {'code': r.status_code, 'message': r.text}})


@app.route('/login', methods=['POST'])
def login():
    login_ = data.login(request.form['email'],
                        request.form['password'])
    r = transport.login(login_)
    if r.status_code == 200:
        return '<p>Login Success!</p>', 200
    else:
        return f'<p>Login Failed! User with email: {login_["email"]}, ' \
               f'and password: {login_["password"]} does not exist</p>', 200


@app.route('/login')
def serve_login_page():
    return render_template('login.html')


@app.route('/register')
def serve_register_page():
    return render_template('register.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
