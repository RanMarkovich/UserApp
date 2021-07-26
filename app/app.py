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
        return render_template('messages.html', message='Register Success'), 200
    elif r.status_code == 409:
        return render_template('messages.html', message=f'Registration failed!',
                               details=f'user with email "{user["email"]}" already exist!'), 409
    else:
        return jsonify({'error': {'code': r.status_code, 'message': r.text}})


@app.route('/login', methods=['POST'])
def login():
    login_ = data.login(request.form['email'],
                        request.form['password'])
    r = transport.login(login_)
    if r.status_code == 200:
        return render_template('messages.html', message='Login Success'), 200
    else:
        return render_template('messages.html', message=f'Login Failed! check your details',
                               details=f'Email: {login_["email"]} , Password: {login_["password"]}'), 200


@app.route('/login')
def serve_login_page():
    return render_template('login.html')


@app.route('/register')
def serve_register_page():
    return render_template('register.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
