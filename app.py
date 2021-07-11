from flask import Flask, render_template, request

from database.database import Database

app = Flask(__name__)
db = Database()


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['fname']
    last_name = request.form['lname']
    user_name = request.form['uname']
    email = request.form['email']
    password = request.form['password']
    db.create_user(first_name, last_name, user_name, email, password)
    return 'registered!', 200


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if db.validate_user(email, password):
        return 'Login Success!', 200
    else:
        return f'Login Failed! User with email: {email}, and password: {password} does not exist', 200


@app.route('/login')
def serve_login_page():
    return render_template('login.html')


@app.route('/register')
def serve_register_page():
    return render_template('register.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
