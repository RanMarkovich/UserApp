from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)

user = {'firstName': 'firstName',
        'lastName': 'lastName',
        'userName': 'userName',
        'email': 'email',
        'password': 'password'}


@app.route('/register', methods=['POST'])
def register():
    global user
    user['firstName'] = request.form['fname']
    user['lastName'] = request.form['lname']
    user['userName'] = request.form['uname']
    user['email'] = request.form['email']
    user['password'] = request.form['password']
    r = requests.post('http://user-service:5000/register', json=user)
    if r.status_code == 200:
        return 'registered!', 200
    else:
        return jsonify(r.text), r.status_code




# @app.route('/login', methods=['POST'])
# def login():
#     email = request.form['email']
#     password = request.form['password']
#     if db.validate_user(email, password):
#         return 'Login Success!', 200
#     else:
#         return f'Login Failed! User with email: {email}, and password: {password} does not exist', 200
#

@app.route('/login')
def serve_login_page():
    return render_template('login.html')


@app.route('/register')
def serve_register_page():
    return render_template('register.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
