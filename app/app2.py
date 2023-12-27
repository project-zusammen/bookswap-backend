from flask import Flask, request, jsonify
# from db import init_app, db
# from models import User
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
# init_app(app)
# bcrypt = Bcrypt(app)

# Routes for user registration and login


@app.route('/', methods=['GET'])
def index():
    return {"Hello": "BOOKSWAP"}

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     hashed_password = bcrypt.generate_password_hash(
#         data['password']).decode('utf-8')
#     new_user = User(username=data['username'], password=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'message': 'User registered successfully'})


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user = User.query.filter_by(username=data['username']).first()
#     if user and bcrypt.check_password_hash(user.password, data['password']):
#         return jsonify({'message': 'Login successful'})
#     else:
#         return jsonify({'message': 'Invalid username or password'})


if __name__ == '__main__':
    app.run(debug=True, port=5555)
