from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(data):
    # Extract user data from the request
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if the user already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return {'message': 'User already exists.'}, 409

    # Create a new user
    new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'User registered successfully.'}, 201

def login_user(data):
    # Extract login data from the request
    username = data.get('username')
    password = data.get('password')

    # Find the user by username
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and the password is correct
    if user and check_password_hash(user.password, password):
        # Implement your login logic here (e.g., creating a session)
        return {'message': 'Login successful.'}, 200

    return {'message': 'Invalid username or password.'}, 401

def logout_user():
    # Implement your logout logic here (e.g., destroying the session)
    return {'message': 'Logout successful.'}, 200
